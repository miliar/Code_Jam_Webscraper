#include<iostream>
using namespace std;

int main(){
int nc;
cin>>nc;
for(int i=0;i<nc;i++){
	int a,b,temp,temp1,temp2,temp3,ar1[4],ar2[4],ans=0,result;
	cin>>a;
	for(int j=0;j<4;j++){
		if(j+1==a){
		cin>>ar1[0]>>ar1[1]>>ar1[2]>>ar1[3];
			}
		else {
			cin>>temp>>temp1>>temp2>>temp3;
			}
		}
		cin>>b;
	for(int j=0;j<4;j++){
		if(j+1==b){
		cin>>ar2[0]>>ar2[1]>>ar2[2]>>ar2[3];
			}
		else {
			cin>>temp>>temp1>>temp2>>temp3;
			}
		}
	for(int j=0;j<4;j++){
		for(int k=0;k<4;k++){
			if(ar1[j]==ar2[k]){
				ans++;
				result=ar1[j];
				}
			}
		
		}
		
		if(ans==0){
			cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
			}
		else if(ans==1){
			cout<<"Case #"<<i+1<<": "<<result<<endl;
			}
		else {
			cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
			}
	}


}
