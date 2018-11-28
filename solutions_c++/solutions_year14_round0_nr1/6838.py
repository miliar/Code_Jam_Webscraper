#include<iostream>
using namespace std;

int main(){
	int T,iter=1;
	int mat1[4],mat2[4];
	int first,sec,matches,temp,val;
	cin>>T;
	while(T--){
		cin>>first;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(i==first-1) cin>>mat1[j];
				else cin>>temp;		
			}		
		}
		cin>>sec;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(i==sec-1) {
					cin>>mat2[j];
				}
				else cin>>temp;		
			}		
		}
		matches=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(mat1[i]==mat2[j]) {
					matches++;
					val=mat1[i];
				}
			}
		}
		cout<<"Case #"<<iter<<": ";
		if(matches==0) cout<<"Volunteer cheated!";
		else if(matches==1) cout<<val;
		else cout<<"Bad magician!";
		cout<<endl;
	
		iter++;
	}




}
