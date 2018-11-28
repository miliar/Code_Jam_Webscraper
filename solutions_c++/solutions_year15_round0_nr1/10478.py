#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main(int argc, char** argv) {
	// your code goes here
	int T=0;
	cin>>T;
	for(int n=0;n<T;++n){
		cout<<"Case #"<<n+1<<": ";
		int sMax=0;
		cin>>sMax;
		//scanf("%d",&sMax);
		string Shy;
		cin>>Shy;
		/*
		int length=0;
		for(int m=0;m<=sMax;++m){
			cin>>Shy[m];
			//scanf("%d",&Shy[m]);
			//cout<<Shy[m]<<endl;
			length++;
		}
		*/
		int standingPeople=0;
		int addFrds=0;
		for(int i=0;i<=sMax;++i){
			int tmp = Shy[i] - '0';
			if(Shy[i]==0)
			continue;
			
			if(i <= standingPeople)
				standingPeople+=tmp;
			else
			{
				addFrds+=i-standingPeople;
				standingPeople+=i-standingPeople+tmp;
			}
			//cout<<standingPeople<<","<<addFrds<<","<<i<<","<<tmp<<endl;
		}
		cout<<addFrds<<endl;
	}
	return 0;
}
