#include<iostream>
#include<algorithm>
using namespace std;
int solve(){
	int x, r, c;
	int flag=0; //Richard
	cin>>x>>r>>c;
	if(x>r*c)return 0;
	if(x==1)return 1;
	if(x==2){
		if((r*c)%2==1 ||(r*c==1))return 0;
		return 1;
	}
	if(x==3){
		if(r*c==3)return 0;
		if(r*c==4)return 0;
		if(r*c==6)return 1;
		if(r*c==8)return 0;
		if(r*c==9)return 1;
		if(r*c==12)return 1;
		if(r*c==16)return 0;
		//1x3, //1x4, 2x2, 2x3, 2x4, 3x3, 3x4, 4x4
	}
	if(x==4){
		if(r*c==4)return 0;
		if(r*c==6)return 0;
		if(r*c==8)return 0;
		if(r*c==9)return 0;
		if(r*c==12)return 1;
		if(r*c==16)return 1;
	}
	return 1;
}
int main(){
	int t;
	cin>>t;
	for(int i=1; i<=t; i++)cout<<"Case #"<<i<<": "<<(solve()==0?"RICHARD":"GABRIEL")<<endl;
	return 0;
}
