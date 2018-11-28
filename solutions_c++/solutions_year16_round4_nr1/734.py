#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;

//P,R,S
char wins[128];
string solve(int dep,char t){
	if(!dep)return string(1,t);
	string res1=solve(dep-1,t);
	string res2=solve(dep-1,wins[t]);
	if(res1<res2)return res1+res2;
	return res2+res1;
}
string arr[3];

int t,n,R,P,S;
bool ok(int idx){
	int r=0,p=0,s=0;
	lop(i,arr[idx].size()){
		if(arr[idx][i]=='R')++r;
		if(arr[idx][i]=='P')++p;
		if(arr[idx][i]=='S')++s;
	}
	if(r!=R||p!=P||s!=S)return 0;
	return 1;
}
int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	wins['R']='S';
	wins['S']='P';
	wins['P']='R';
	sc(t);
	lop(C,t){
		sc(n),sc(R),sc(P),sc(S);
		arr[0]=solve(n,'R');
		arr[1]=solve(n,'P');
		arr[2]=solve(n,'S');
		sort(arr,arr+3);
		bool found=0;
		lop(i,3)if(ok(i)){
			printf("Case #%d: %s\n",C+1,arr[i].c_str());
			found=1;
			break;
		}
		if(!found)printf("Case #%d: IMPOSSIBLE\n",C+1);
	}


};
