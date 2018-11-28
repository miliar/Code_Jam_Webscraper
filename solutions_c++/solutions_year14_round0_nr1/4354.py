#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
int T;
cin>>T;
for(int i=1; i<=T; i++){
	int firstans;
	cin>>firstans;
	int firstsq[4][4];
	for(int r=0; r<4;r++){
		for(int c=0; c<4;c++){
		cin>>firstsq[r][c];
		}
	}
	
	int secans;
	cin>>secans;
	int secsq[4][4];
	for(int r=0; r<4;r++){
		for(int c=0; c<4;c++){
		cin>>secsq[r][c];
		}
	}
	
	int ans;
	int count=0;
	for(int x=0; x<4; x++){
		for(int y=0; y<4; y++){
		if(firstsq[firstans-1][x]==secsq[secans-1][y]){
			count++;
			ans=firstsq[firstans-1][x];
		}
		}
	}
	
	if(count==1){
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	else if(count>1){
		cout<<"Case #"<<i<<": Bad magician!"<<endl;
	}
	else{
		cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
	}
		
}
}

/*
 * cout<<firstans<<endl;
		
			for(int r=0; r<4;r++){
				for(int c=0; c<4;c++){
				cout<<firstsq[r][c]<<" ";
				}
				cout<<endl;
			}
		
		cout<<endl<<secans<<endl;
		
			for(int r=0; r<4;r++){
				for(int c=0; c<4;c++){
				cout<<secsq[r][c]<<" ";
				}
				cout<<endl;
			}
		cout<<endl;
 */ 
