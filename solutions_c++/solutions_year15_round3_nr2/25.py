#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:10000000000")
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

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define INF 1e8
#define EPS 1e-8
#define MOD 1000000007
#define SQR(a) ((a)*(a))
typedef long long  ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;


int mynext[200];

void prekmp(const string & s){
	mynext[0]=-1;
	for (int i=1;i<=s.size();++i){
		mynext[i] = mynext[i-1];
		while (mynext[i]>=0 && s[mynext[i]] != s[i-1])
			mynext[i] = mynext[mynext[i]];
		++mynext[i];
	}
}

string s,t;
double p;
double memo[110][110][110];
double memo2[110][110][110];

double f(int remains,int cur,int q){
	if(remains==0) {
		return q==t.size()?1:0;
	}
	
	double res=0;
	double &ret=memo[remains][cur][q];
	if(ret>-0.5) return ret;
	while(q>-1 && s[cur]!=t[q] ) q = mynext[q];q++;
	
	FR(i,s.size()){
		if(q == t.size()) res+=p*(1+f(remains-1,i,mynext[q]));
		else res+=p*(f(remains-1,i,q));
	}
	
	return ret=res;

}

double f2(int remains,int cur,int q){
	if(remains==0) {
		return q==t.size()?1:0;
	}
	
	double res=0;
	double &ret=memo2[remains][cur][q];
	if(ret>-0.5) return ret;
	
	while(q>-1 && s[cur]!=t[q] ) q = mynext[q];q++;
	
	FR(i,s.size()){
		if(q == t.size()) res=max(res,1+f2(remains-1,i,mynext[q]));
		else res=max(res,f2(remains-1,i,q));
	}
	
	return ret=res;

}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int cas;cin>>cas;
	FR(mycas,cas){
		printf("Case #%d: ",mycas+1);
		int tt,len;
		cin>>tt>>tt>>len;
		
		cin>>s>>t;
		CLR(memo,-1);
		CLR(memo2,-1);
		double expectedBanana = 0;
		p=1./(s.size());
		prekmp(t);
		FR(i,s.size()){
			expectedBanana += p*f(len,i,0);
		}
		double maxi=0;
		FR(i,s.size()){
			maxi=max(maxi,f2(len,i,0));
		}
		cout<<fixed<<setprecision(10)<<maxi-expectedBanana<<endl;
	}

}