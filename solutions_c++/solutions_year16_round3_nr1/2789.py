#include<iostream>

using namespace std;


int* findPair(int* s, int N){
	int* res = new int[2];

	int maxVal = 0;
	int maxAt = -1;
	for(int i=0; i<N; i++){
		if(s[i] > maxVal){
			maxAt = i;
			maxVal = s[i];
		}
	}

	int nextMaxVal = 0;
	int nextMaxAt = -1;

	for(int i=0; i<N; i++){
		if(i != maxAt && s[i] > nextMaxVal){
			nextMaxVal = s[i];
			nextMaxAt = i;
		}
	}

	res[0] = maxAt;
	res[1] = nextMaxAt;

	return res;
}


int main(){
	int T;
	cin>>T;

	int atCase = 0;
	while(atCase < T){
		int N;
		cin>>N;

		int* senate = new int[N];

		int numSen = 0;
		for(int i=0; i<N; i++){
			cin>>senate[i];
			numSen += senate[i];
		}

		cout<<"Case #"<<atCase+1<<": ";

		if(numSen % 2 == 1){
			int* t = findPair(senate,N);
			cout<<(char)(65+t[0])<<" ";
			senate[t[0]]--;
			numSen--;
		}

		while(numSen > 0){
			int* t = findPair(senate,N);
			cout<<(char)(65+t[0])<<(char)(65+t[1])<<" ";
			senate[t[0]]--;
			senate[t[1]]--;
			numSen -= 2;
		}
		cout<<endl;

		atCase++;
	}
}
