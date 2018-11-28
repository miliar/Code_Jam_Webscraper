#include <iostream>
#include <cmath>
#include <vector>
using namespace std;


int ans[20][3];

void getSeq(){
	ans[1][0]=1;
	ans[1][1]=1;
	ans[1][2]=0;
	for(int l=2;l<18;l++){
		ans[l][0]=ans[l-1][0]+ans[l-1][2];
		ans[l][1]=ans[l-1][1]+ans[l-1][0];
		ans[l][2]=ans[l-1][2]+ans[l-1][1];
	}
}
string oneL(int c){
	if(c==0)return "P";
	if(c==1)return "R";
	if(c==2)return "S";
	return "!";
}
string printCorrect(int l,int c){//c==012
	if(l==0)return oneL(c);
	string s1=printCorrect(l-1,c);//winner
	string s2=printCorrect(l-1,(c+1)%3);//loser
	if(s1<s2)return s1+s2;
	else return s2+s1;
}

void Calc(){
	int l;
	int r,p,s;
	cin>>l;
	cin>>r>>p>>s;

	if(p==ans[l][0] && r==ans[l][1] && s==ans[l][2]){
		cout<<printCorrect(l,0)<<endl;
		return;
	}
	if(p==ans[l][2] && r==ans[l][0] && s==ans[l][1]){
		cout<<printCorrect(l,1)<<endl;
		return;
	}
	if(p==ans[l][1] && r==ans[l][2] && s==ans[l][0]){
		cout<<printCorrect(l,2)<<endl;
		return;
	}
		cout<<"IMPOSSIBLE"<<endl;

	//
	//int l=3;
	//printf("l=3 %d %d %d\n",ans[l][0],ans[l][1],ans[l][2]);
}

int main(){
	getSeq();

	int T;cin>>T;for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		Calc();
	}
	return 0;
}
