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
typedef pair<int,int>	pii;
typedef long long ll;
int f,s,a[4][4],b[4][4];
int main(){
	iosfal;
	int T;
	cin >> T;
	For(test,0,T){
		cout << "Case #"<<test+1<<": ";
		cin >> f;
		For(i,0,4)
			For(j,0,4)
				cin >> a[i][j];
		cin >> s;
		For(i,0,4)
			For(j,0,4)
				cin >> b[i][j];
		set<int> w,e,ans;
		-- f;
		-- s;
		For(i,0,4)
			w.insert(a[f][i]),
			e.insert(b[s][i]);
		For(i,1,17)
			if(w.find(i) != w.end() && e.find(i) != e.end())
				ans.insert(i);
		if(!ans.size())
			cout << "Volunteer cheated!\n";
		else if(ans.size() > 1)
			cout << "Bad magician!\n" ;
		else
			cout << *(ans.begin()) << endl;


	}
}
