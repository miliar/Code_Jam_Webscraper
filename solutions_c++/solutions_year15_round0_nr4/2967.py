#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main(){
freopen("D-small-attempt0.in","r",stdin);
freopen("out.txt","w",stdout);
int t,x,r,c;
cin>>t;
for(int k=1;k<=t;k++){
	cin>>x>>r>>c;
	if(x==1){
		cout<<"Case #"<<k<<": GABRIEL"<<endl;
	}else if(x==2){
		if((r*c)%2){
			cout<<"Case #"<<k<<": RICHARD"<<endl;
		}else{
			cout<<"Case #"<<k<<": GABRIEL"<<endl;
		}}else if(x==3){
			if((r==2&&c==3)||(r==3&&c==2)||(r==3&&c==3)||(r==4&&c==3)||(r==3&&c==4))
			cout<<"Case #"<<k<<": GABRIEL"<<endl;
			else
			cout<<"Case #"<<k<<": RICHARD"<<endl;
		}else if(x==4){
			if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4))
			cout<<"Case #"<<k<<": GABRIEL"<<endl;
			else
			cout<<"Case #"<<k<<": RICHARD"<<endl;		
		}
	}
}	

