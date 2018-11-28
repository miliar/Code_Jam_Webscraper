#include <iostream>
#include <cstdlib>
using namespace std;
int main(void){
int testCase;
int numInt;
int value;
int totalPeople;
int invitePeople;
int nValue;


cin>> testCase;
for(int z = 1; z<=testCase; z++){
cin>> numInt;
numInt++;
int outputArray[numInt];

cin>>value;
for(int i = numInt-1; i>=0;i--){
	nValue = value%10;
	value=value/10;
	outputArray[i]= nValue;
}
totalPeople=0;
invitePeople=0;
for(int m = 0; m<numInt;m++){
	totalPeople=outputArray[m]+totalPeople;
	if(totalPeople<=m){
		invitePeople++;
		totalPeople++;
	}
}

cout<<"Case #"<<z<<": "<<invitePeople<<endl;
}
return 0;
}

