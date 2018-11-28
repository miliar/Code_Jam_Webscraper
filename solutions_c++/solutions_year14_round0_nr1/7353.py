// iHaala Madrid - A Gunner
#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

int main(){
	int t,i,j,x,y;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		int cnt[17]={0};
		cin>>x;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){							
				cin>>y;
				if(i==x)	cnt[y]++;
			}
		}
		cin>>x;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){							
				cin>>y;
				if(i==x)	cnt[y]++;
			}
		}
		
		for(i=1,x=0,y=-1;i<=16;i++){
			if(cnt[i]==2){
				x++;
				y=i;
			}
		}
		
		cout<<"Case #"<<tt<<": ";
		
		if(x==1){
			cout<<y;
		}else if(x>1){
			cout<<"Bad magician!";
		}else{
			cout<<"Volunteer cheated!";
		}
		
		cout<<endl;
	}
	
	return 0;	
}