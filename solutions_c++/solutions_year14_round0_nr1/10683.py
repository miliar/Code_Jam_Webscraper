#include<iostream>
using namespace std;

bool ism(int a,int b[],int c){
for(int i = 0; i < c; i++){
	if(b[i] == a) return true;
}
return false;
}
	

int main(int arc,char* argv[]){
int numcase;
cin>>numcase;

int a1[4][4];
int a2[4][4];
int r1,r2;

for(int k = 0; k < numcase;k++){
	cin>>r1;
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++) {
			cin>>a1[i][j];
		}
	}	
	cin>>r2;
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++) {
			cin>>a2[i][j];
			
		}
	}
	int a = 0,t;
	for(int i = 0; i < 4; i++){
		if(ism(a1[r1-1][i],a2[r2-1],4)){a++;t = i;}
	}
	cout<<"Case #"<<k+1<<": ";
	if(a == 1) cout<<a1[r1-1][t]<<endl;
	if(a == 0) cout<<"Volunteer Cheated!"<<endl;
	if(a > 1) cout<<"Bad magician!"<<endl;
}



}
