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


int countbit(int n){
	int num=0;
	while(n>0){
		if(n&1) num++;
		n>>=1;
	}
	return num;
}

string s[20],t[20];
int n;
bool isok(int mask){
	FR(i,n){
		if(!(1<<i)&mask) continue;
		bool is1=false,is2=false;
		FR(j,n){
			if((1<<j)&mask) continue;
			if(s[i]==s[j]) is1=true;
			if(t[i]==t[j]) is2=true;
		}
		if(!is1 || !is2) return false;
	}
	return true;
}
int main(){
	freopen("a.in","r",stdin);	
	freopen("a.out","w",stdout);
	int tt;cin>>tt;
	FR(cas,tt){
		printf("Case #%d: ",cas+1);
		
		cin>>n;
		FR(i,n) cin>>s[i]>>t[i];
		int res=0;
		FR(i,(1<<n)){
			if(isok(i))
				res=max(res,countbit(i));
		}
		cout<<res<<endl;
	}
}