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


string my_sort(string s){
	if(s.size()<=1) return s;
	string s1=s.substr(0,s.size()/2);
	string s2=s.substr(s.size()/2);
	s1=my_sort(s1);
	s2=my_sort(s2);
	if(s1<s2) return s1+s2;
	return s2+s1;

}

int main(){
	freopen("a.in","r",stdin);	
	freopen("a.out","w",stdout);
	string s[3][13];
	s[0][0]="P";
	s[1][0]="R";
	s[2][0]="S";
	FR(i,3){
		FR(j,12)
			FR(k,s[i][j].size()){
				string temp;
				if(s[i][j][k]=='P') temp="RP";
				if(s[i][j][k]=='R') temp="RS";
				if(s[i][j][k]=='S') temp="SP";
				s[i][j+1] += temp;
		}
	}

	int count[3][13][3]={0};
	FR(i,3)FR(j,13)FR(k,s[i][j].size()){
		if(s[i][j][k]=='P') count[i][j][0]++;
		if(s[i][j][k]=='R') count[i][j][1]++;
		if(s[i][j][k]=='S') count[i][j][2]++;
	}
	
	FR(i,3)FR(j,13) s[i][j] = my_sort(s[i][j]);

	int tt;cin>>tt;
	FR(cas,tt){
		printf("Case #%d: ",cas+1);
		int n,r,p,ss;
		cin>>n>>r>>p>>ss;
		string res="Z";
		FR(i,3)
			if(count[i][n][0]==p && count[i][n][1]==r && count[i][n][2]==ss) 
				res=min(res,s[i][n]);
		cout<<(res=="Z"?"IMPOSSIBLE":res)<<endl;
	}
}