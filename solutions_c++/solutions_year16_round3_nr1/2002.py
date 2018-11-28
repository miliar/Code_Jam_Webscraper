#include <bits/stdc++.h>

using namespace std;

int P[30];
int N;

vector<int> findMax(){
	int max = 0;
	int index = 0;
	vector<int> ret;
	for(int i=0; i<N; i++){
		if(P[i]>max){
			max = P[i];
			index = i;
		}
	}
	ret.push_back(index);

	max = 0;
	for(int i=0; i<N; i++){
		if(i==ret[0]) continue;

		if(P[i]>max){
			max = P[i];
			index = i;
		}
	}

	ret.push_back(index);

	return ret;
}

int main(){
	int T;
	cin>>T;

	for(int K=1; K<=T; K++){
		string ans = "";

		cin>>N;
		int sum = 0;
		for(int i=0; i<N; i++){
			cin>>P[i];
			sum+=P[i];
		}

		vector<int> majorIndex = findMax();
		// cout<<majorIndex[0]<<" "<<majorIndex[1]<<endl;
		while(P[majorIndex[0]] != P[majorIndex[1]]){
			ans+= 'A' + majorIndex[0];
			ans+= " ";
			P[majorIndex[0]]--;
			sum--;
		}
		// cout<<"Lolos"<<endl;

		for(int i=0; i<N; i++){
			if(i==majorIndex[0] || i==majorIndex[1])
				continue;

			while(P[i]){
				ans+= 'A' + i;
				ans+= " ";
				P[i]--;
				sum--;
			}
		}

		while(P[majorIndex[0]]){
			ans+= 'A' + majorIndex[0];
			ans+= 'A' + majorIndex[1];
			if(P[majorIndex[0]] != 1)
				ans+= " ";
			P[majorIndex[0]]--;
			P[majorIndex[1]]--;
			sum--;
		}

		cout<<"Case #"<<K<<": "<<ans<<endl; 
	}

	return 0;
}