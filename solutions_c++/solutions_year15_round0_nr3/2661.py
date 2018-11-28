//============================================================================
// Name        : Contest.cpp
// Author      : Alireza
// Version     :
// Copyright   : Enjoy It!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstring>
#include <queue>
#include <functional>

#define FOR(i,c,n) for(int i=(c);(i)<(n);++(i))
#define FR(i,n) FOR(i,0,n)
using namespace std;

int a[4][4]={
		{0,1,2,3},
		{1,4,3,6},
		{2,7,4,1},
		{3,2,5,4}
};
string s;
int memo[220000][8][3];
bool f(int ind,int cur,int turn){
	if(ind==s.size()){
		if(turn==2 && cur==3) return true;
		return false;
	}
	int &ret=memo[ind][cur][turn];
	if(ret!=-1) return ret;
	bool res = false;
	int now = cur<4 ? a[cur][s[ind]-'0'] : (a[cur-4][s[ind]-'0']+4)%8;
	res |= f(ind+1,now,turn);
	if((turn==0 && now==1) || (turn==1 && now==2)) res |= f(ind+1,0,turn+1);
	return ret=res;
}

int main() {
	freopen("/home/alireza/Downloads/C-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);
	int tcase;cin>>tcase;
	FR(cas,tcase){
		printf("Case #%d: ",cas+1);
		long long l,x,xx;
		cin>>l>>x;xx=x;
		xx%=4;while(xx<18)xx+=4;
		x=min(xx,x);
		string ss;cin>>ss;
		s.clear();
		FR(i,x) s+=ss;
		FR(i,s.size()){
			if(s[i]=='i') s[i]='1';
			if(s[i]=='j') s[i]='2';
			if(s[i]=='k') s[i]='3';
		}
		memset(memo,-1,sizeof(memo));
		cout<<(f(0,0,0)==1?"YES":"NO")<<endl;
	}
}
