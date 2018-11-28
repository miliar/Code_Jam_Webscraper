#include <iostream>
#include <cstdlib>
using namespace std;

void updateAll(int *a,int start, int length, int increment);

int main(){
	int testNumber=0;
	cin>>testNumber;
	int loopCounter=0;
	while(loopCounter<testNumber){
		int prevStandingPeople[1005]={0};
		int Smax=0,temp=0,addPeople=0,totalAddedPeople=0;
		char sample[1005];
		cin>>Smax;
		cin>>sample;
		prevStandingPeople[0]=0;
		//cout<<sample<<endl;
		for(int i=1;i<=Smax+1;++i){
			prevStandingPeople[i]=prevStandingPeople[i-1]+sample[i-1]-'0';
			addPeople=prevStandingPeople[i]-i;
			if(addPeople<0){
				totalAddedPeople-=addPeople;
				prevStandingPeople[i]-=addPeople;
			}
		}
		cout<<"Case #"<<loopCounter+1<<": "<<totalAddedPeople<<endl;
		loopCounter++;
	}
}