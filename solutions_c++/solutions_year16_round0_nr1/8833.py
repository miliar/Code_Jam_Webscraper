#include <iostream>

using namespace std;

int main(){
	int T;

		int N,M;
	bool table[10];
	int c;
	int count;
	int i;
	int L;

	cin>>T;


	for(int casenum=1;  casenum<=T; casenum++){
		cin>>N;
		if(N==0){
			cout<<"Case #"<<casenum<<": INSOMNIA\n";
			continue;
		}
		for(i=0; i<10; i++){
			table[i]=true;
		}

		count=0;
		M=N;
		L=N;
		for(i=0; i<100000; i++){
			c=M%10;
			M/=10;
			/*
			for(int j=0; j<10; j++){
				cout<<table[j]<<" ";
			}
			cout<<endl;
			*/
			if(table[c]){
				table[c]=false;
				count++;
			}
			if(count==10){
				cout<<"Case #"<<casenum<<": "<<L<<endl;
				break;
			}
			if(M==0){
				M=L+N;
				L=M;
			}
		}
		if(i==100){
			cout<<"Case #"<<casenum<<": INSOMNIA\n";
		}

	}

	return 0;
}
