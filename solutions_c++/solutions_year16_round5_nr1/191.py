#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
string s;
int num[5][5];
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		cin>>s;int n=s.size();
		memset(num,0,sizeof(num));
		rep(j,n){
			if(s[j]=='C') num[j%2][0]++;
			else num[j%2][1]++;
		}
		printf("Case #%d: %d\n",i+1,(min(num[0][0],num[1][0])+min(num[0][1],num[1][1])+n/2)*5);
	}
}
