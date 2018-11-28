#include<iostream>
using namespace std;
int main(){
	int ntest,guess1,guess2,a[4][4],b[4][4];
	cin>>ntest;
	for(int k=0;k<ntest;k++){	
		int correct=0;
		int pres;
		cin>>guess1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>a[i][j];
			}
		}
		cin>>guess2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>b[i][j];
			}
		}
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a[guess1-1][i]==b[guess2-1][j])
				{correct++;
				pres=a[guess1-1][i];}
			}
		}
		
		switch(correct){
			case 0: cout<<"Case #"<<k+1<<": Volunteer cheated!"<<endl;break;
			case 1: cout<<"Case #"<<k+1<<": "<<pres<<endl;break;
			default: cout<<"Case #"<<k+1<<": Bad magician!"<<endl;break;
		}
		}
	}
		
				
