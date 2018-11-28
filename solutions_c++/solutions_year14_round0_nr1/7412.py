#include <iostream>
#include <string>
using namespace std;

int main(){
	int FC,SC,FA[4][4],FB[4][4],FL[4],SL[4],CASE=1,i,z,Count=0,t;
	cin>>t;
	for(CASE = 1;CASE<=t;CASE++){
    int arr[t];
    cin>>FC;
	for(i=0;i<4;i++){
		for(z=0;z<4;z++){
			cin>>FA[i][z];
		}
	}
	cin>>SC;
	for(i=0;i<4;i++){
		for(z=0;z<4;z++){
			cin>>FB[i][z];
		}
	}


	for(i=0;i<4;i++){
        FL[i] = FA[FC-1][i];                 
        SL[i] = FB[SC-1][i];
    }
    Count = 0;
	for(i=0;i<4;i++){
		for(z=0;z<4;z++){
			if(FL[i]==SL[z]){
                 Count++;
			     arr[CASE-1]=FL[i];
            }
		}
	}
	if(Count==1){
		cout<<"Case #"<<CASE<<": "<<arr[CASE-1]<<endl;
	}else if(Count==0){
		cout<<"Case #"<<CASE<<": "<<"Volunteer cheated!"<<endl;
	}else{
		cout<<"Case #"<<CASE<<": "<<"Bad magician!"<<endl;
	}
 }
	
}
