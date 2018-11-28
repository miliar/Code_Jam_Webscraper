//GCJ - Pre Elimination B
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<utility>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<list>
#include<cstring>
#include<string>
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front
#define OO (int)2e9
#define INF (ll)9e18
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
using namespace std;

int t,l,res;
char s[105];

int ser(int len){
	int ret,rett=0,pos,poss;
	repp(i,0,len){
		if(s[i]=='+'&&s[i+1]=='-')pos=i;
		if(s[i]=='-'&&s[i+1]=='+'){
			ret=poss=i+1;
			break;
		}
	}
	repp(i,poss,len){
		if(s[i]=='+')rett++;
		if(s[i]=='-'){
			if(rett>ret){
				ret=rett;
				pos=i-1;
			}
			rett=0;
		}
	}
	return pos;
}

void check(int len){
	char c;
	repp(i,0,len/2){
		c=s[i];
		s[i]=s[len-i];
		s[len-i]=c;
	}
	repp(i,0,len){
		if(s[i]=='+')s[i]='-';
		else s[i]='+';
	}
}

int pro(int len){
	if(len<0)return 0;
	if(s[len]=='+')return pro(len-1);
	//else
	if(s[0]=='-'){
		check(len);
		return 1+pro(len-1);
	}
	else{
		int p=ser(len-1);
		check(p);
		check(len);
		return 2+pro(len-1);
	}
}

int main(){
	scanf("%d",&t);
	repp(tc,1,t){
		scanf("%s",s);
		l=strlen(s);
		res=pro(l-1);
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}
