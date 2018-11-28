#include<iostream>
#include<cmath>
#include<math.h>
#include<string>
#include<cstring>
#include<cstdio>
#include<cctype>
#include<cstdlib>
#include<stdio.h>
#include<vector>
#include<set>
#include<map>
#include<fstream>
#include<sstream>
#include<list>
#include<iomanip>
#include<algorithm>
#include<stack>
#include<deque>
#include<queue>
#include<bitset>
#include<cstddef>
#include<complex>
#include<ctime>
using namespace std;
#define Foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i,a,b)  for( int i=(a);i<(b);i++)
#define back(i,a,b) for( int i=(a);i>(b);i--)
#define	ff    first
#define ss	second
#define un  unsigned
#define pb  push_back
#define PB  pop_back()
#define iosfal  ios_base::sync_with_stdio(false)
#define mp(a,b) make_pair(a,b)
#define sqr(a)  (a)*(a)
#define all(a)  a.begin() , a.end()
#define error(x) cerr << #x << " = " << (x) <<endl
#define erorr(x) fout<<#x<<" = "<<(x)<<endl
#define Error(a,b) cerr<<"( "<<#a<<" , "<<#b<<" ) = ( "<<(a)<<" , "<<(b)<<" )\n";
#define errop(a) cerr<<#a<<" = ( "<<((a).ff)<<" , "<<((a).ss)<<" )\n";
#define coud(a,b) cout<<fixed << setprecision((b)) << (a) <<endl
#define nalpha  noboolalpha 
#define max(x,y)	((x)>(y)?(x):(y))
#define min(x,y)	((x)<(y)?(x):(y))
#define CEIL(x)	((x)/2 + 1)
#define dist(i,f,a)	(double)((double)(a)/(double)((2.0)+(f)*((double)i)))
typedef pair<int,int>	pii;
typedef long long ll;
const int maxn = 100000+100;
double t[maxn];
double c,f,x;
int main(){
	iosfal;
	int T;
	cin >> T;
	For(test,0,T){
		cout << "Case #"<<test+1<<": ";
		cin >> c >> f >> x;
		t[0] = 0.0;
		double ans = dist(0.0,f,x);
		For(i,1,maxn){
			t[i] = t[i-1] + dist(i-1LL,f,c);
			ans = min(ans,t[i] + dist(i,f,x));
		}
		coud(ans,8);
	}
}
