#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include<deque>
#include<stack>
#include<ctime>
#include<bitset>
#include<set>
using namespace std;
typedef long long ll;
ll pval[20];
string s1,s2; 
string ans1,ans2;
ll mindis;
void dfs(ll v,int p,string &s1, string &s2) {
	if(p==s1.length()) {
		if(abs(v)<mindis) {
			ans1 = s1;
			ans2 = s2;
			mindis = abs(v);
		} else if(abs(v)==mindis) {
			if(ans1 > s1 || (ans1==s1&&ans2>s2)) {
				ans1 = s2;
				ans2 = s2;
			}
		}
		return;
	}
	bool f1,f2;
	f1 = (s1[p]=='?');
	f2 = (s2[p]=='?');
	if(v==0) {
		if(f1)
			s1[p] = '0';
		if(f2)
			s2[p] = '0';
		dfs(v,p+1,s1,s2); 
		if(f1)
			s1[p] = '?';
		if(f2)
			s2[p] = '?';
		return;
	}
	if(v>0) {
		if(f1)
			s1[p] = '0';
		if(f2) {
			int i;
			for(i=1;i<=9;++i) {
				if(v-i*pval[p] < 0)
					break;
			} 
			s2[p] = '0' + i - 1;
			dfs(v - (i-1)*pval[p],p+1,s1,s2);
			if(i!=10) {
				s2[p] = '0' + i;
				dfs(v - i*pval[p],p+1,s1,s2);
			}
			s2[p] = '?';
		} else {
			dfs(v,p+1,s1,s2);
		}
		if(f1)
			s1[p] = '?';
	}
	if(v<0) {
		if(f2)
			s2[p] = '0';
		if(f1) {
			int i;
			for(i=1;i<=9;++i) {
				if(v+i*pval[p] > 0)
					break;
			} 
			s1[p] = '0' + i - 1;
			dfs(v + (i-1)*pval[p],p+1,s1,s2);
			if(i!=10) {
				s1[p] = '0' + i;
				dfs(v + i*pval[p],p+1,s1,s2);
			}
			s1[p] = '?';
		} else {
			dfs(v,p+1,s1,s2);
		}
		if(f2)
			s2[p] = '?';
	}
}
void gao(){
	cin>>s1>>s2;
	ll x1=0,x2=0;
	for(int i=0;i<s1.length();++i) {
		x1*=10;
		x1+=(s1[i]=='?'?0:s1[i]-'0');
	}
	for(int i=0;i<s2.length();++i) {
		x2*=10;
		x2+=(s2[i]=='?'?0:s2[i]-'0');
	}
	for(int i=s1.length()-1;i>=0;--i){
		if(i==s1.length()-1)
			pval[i]=1;
		else
			pval[i]=pval[i+1]*10;
	}
	mindis = abs(x1-x2);
	ans1 = s1;
	ans2 = s2;
	for(int i=0;i<ans1.length();++i)
 		ans1[i]= (ans1[i]=='?'?'0':ans1[i]);
	for(int i=0;i<ans2.length();++i)
 		ans2[i]= (ans2[i]=='?'?'0':ans2[i]);
	dfs(x1-x2,0,s1,s2);
	cout<<ans1<<' '<<ans2<<endl;
}
void usefile(string fn) {
	freopen((fn+".in").c_str(),"r",stdin);
	freopen((fn+".out").c_str(),"w",stdout);
} 
int main() {
	usefile("B-large"); 
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i) {
		printf("Case #%d: ", i);
		gao();
	}
	return 0;
}