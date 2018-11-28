#include<iostream>
using namespace std;

int main(){
int nc;
cin>>nc;
for(int i=0;i<nc;i++){
	int alpha,beta,temp,lol1[4],lol2[4],ans=0,result;
	cin>>alpha;
	for(int j=0;j<4;j++){
		if(j+1==alpha){
		cin>>lol1[0]>>lol1[1]>>lol1[2]>>lol1[3];
			}
		else {
			cin>>temp>>temp>>temp>>temp;
			}
		}
		cin>>beta;
	for(int j=0;j<4;j++){
		if(j+1==beta){
		cin>>lol2[0]>>lol2[1]>>lol2[2]>>lol2[3];
			}
		else {
			cin>>temp>>temp>>temp>>temp;
			}
		}
	for(int j=0;j<4;j++){
		for(int k=0;k<4;k++){
			if(lol1[j]==lol2[k]){
				ans++;
				result=lol1[j];
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
