#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:100000000000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include<complex>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define SQR(a) ((a)*(a))
typedef long long ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

string s,t;
string resS,resT;
ll ten[20];
ll memo[20][3];

ll f(int ind,bool isRestrict){
	if(ind==s.size()) return 0;
	ll mini = 1LL<<62;
	ll &ret=memo[ind][isRestrict];
	if(ret!=-1) return ret;
	FR(i,10)FR(j,10){
		if(j>i && isRestrict) continue;
		if(isdigit(s[ind]) && s[ind]-'0'!=i) continue;
		if(isdigit(t[ind]) && t[ind]-'0'!=j) continue;
		bool newRestrict = isRestrict;
		if(isRestrict && i>j) newRestrict=false;
		mini=min(mini,f(ind+1,newRestrict)+(i-j)*ten[s.length()-1-ind]);
	}
	return ret=mini;
}

void make(int ind,bool isRestrict){
	if(ind==s.size()) return;
	ll mini = f(ind,isRestrict);
	FR(i,10)FR(j,10){
		if(j>i && isRestrict) continue;
		if(isdigit(s[ind]) && s[ind]-'0'!=i) continue;
		if(isdigit(t[ind]) && t[ind]-'0'!=j) continue;
		bool newRestrict = isRestrict;
		if(isRestrict && i>j) newRestrict=false;
		if(mini == f(ind+1,newRestrict)+(i-j)*ten[s.length()-1-ind])
		{
			resS += (i+'0');
			resT += (j+'0');
			make(ind+1,newRestrict);
			return;
		}
		//mini=min(mini,f(ind+1,newRestrict)+(i-j)*ten[s.length()-1-ind]);
	}
}



int main(){
	freopen("a.in","r",stdin);	
	freopen("a.out","w",stdout);
	ten[0]=1;
	FR(i,19) ten[i+1]=ten[i]*(ll)10;
	int tt;cin>>tt;
	FR(cas,tt){
		printf("Case #%d: ",cas+1);
		cin>>s>>t;
		resS=resT="";
		ll ans = 1LL<<62;
		string ansS,ansT;
		CLR(memo,-1);
		ll res = f(0,true);
		make(0,true);
		if(res<ans){
			ans=res;
			ansS=resS;
			ansT=resT;
		}

		CLR(memo,-1);
		swap(s,t);
		resS=resT="";
		res = f(0,true);
		make(0,true);
		swap(resS,resT);

		if(res<ans){
			ans=res;
			ansS=resS;
			ansT=resT;
		}else if(res==ans){
			if(resS<ansS){
				ansS=resS;
				ansT=resT;
			}else if(resS==ansS){
				ansT=min(resT,ansT); 
			}
		}

		cout<<ansS<<" "<<ansT<<endl;
	}
}