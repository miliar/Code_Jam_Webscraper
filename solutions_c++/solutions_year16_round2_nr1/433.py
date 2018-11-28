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

int a[26];
int getVal(string s,char ch){
	int used = a[ch-'A'];
	FR(i,s.size()) a[s[i]-'A']-=used;
	return used;
}
int main(){
	freopen("a.in","r",stdin);	
	freopen("a.out","w",stdout);
	int t;cin>>t;
	FR(cas,t){
		printf("Case #%d: ",cas+1);
		string s;
		cin>>s;
		FR(i,26)a[i]=0;
		FR(i,s.size()) a[s[i]-'A']++;
		string res;
		int num = 0;
		num=getVal("ZERO",'Z'); FR(i,num) res.push_back('0');
		num=getVal("TWO",'W'); FR(i,num) res.push_back('2');
		num=getVal("FOUR",'U'); FR(i,num) res.push_back('4');
		num=getVal("SIX",'X'); FR(i,num) res.push_back('6');
		num=getVal("EIGHT",'G'); FR(i,num) res.push_back('8');
		num=getVal("SEVEN",'S'); FR(i,num) res.push_back('7');
		num=getVal("ONE",'O'); FR(i,num) res.push_back('1');
		num=getVal("THREE",'T'); FR(i,num) res.push_back('3');
		num=getVal("FIVE",'V'); FR(i,num) res.push_back('5');
		num=getVal("NINE",'E'); FR(i,num) res.push_back('9');

		sort(ALL(res));
		cout<<res<<endl;
	}
}