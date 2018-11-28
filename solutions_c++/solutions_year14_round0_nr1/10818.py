#include<iostream>
using namespace std;

int main(){
int number;
cin>>number;
for(int i=0;i<number;i++){
	int a,b;
	int temp,temp1,temp2,temp3;
	int r1[4],r2[4];
	int ans=0,result;
	cin>>a;
	for(int j=0;j<4;j++){
		if(j+1==a){
		cin>>r1[0]>>r1[1]>>r1[2]>>r1[3];
			}
		else {
			cin>>temp>>temp1>>temp2>>temp3;
			}
		}
		cin>>b;
	for(int j=0;j<4;j++){
		if(j+1==b){
		cin>>r2[0]>>r2[1]>>r2[2]>>r2[3];
			}
		else {
			cin>>temp>>temp1>>temp2>>temp3;
			}
		}
	for(int j=0;j<4;j++){
		for(int k=0;k<4;k++){
			if(r1[j]==r2[k]){
				ans++;
				result=r1[j];
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
