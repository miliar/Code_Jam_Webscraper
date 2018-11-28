#pragma comment(linker,"/STACK:10000000")

//TC

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>

#define forn(a,b,c) for(int (a)=(b);(a)<=(c);(a)++)
#define forr(a,b,c) for(int (a)=(b);(a)>=(c);(a)--)
#define foreach(a,b) for( typeof( (b).begin() ) a=(b).begin(); (a)!=(b).end() ; (a)++ )
#define foreachr(a,b) for( typeof( (b).rbegin() ) a=(b).rbegin(); (a)!=(b).rend() ; (a)++ )
#define dg(x)  cerr <<#x<<':'<<x<<" "
#define dbg(x)  cerr <<#x<<':'<<x<<endl
#define SET(A,b) memset(A,b,sizeof (A) )
#define SIZE(A) ((int)(A).size())
#define ALL(A) (A).begin(),(A).end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define num(a) (1LL<<(a))
using namespace std;

typedef double dbl;
typedef long long Lint;
typedef pair<int,int> ii;
typedef pair<Lint,Lint> Lii;

const Lint mod = 1e9;

const int MAXN = 1000010;

int flip(int k){
	int rev=0;
	while( k>0 ){
		rev*=10;
		rev+=k%10;
		k/=10;
	}
	return rev;
}

int dn[MAXN][2];

int f(int k,int t){
	if(k>MAXN)
		return 1e9;
	int &rev=dn[k][t];

	if(rev!=-1)	return rev;
	if(k==1)	return rev=1;

	rev=1e9;

	if(t==0)
	{
		rev=min(rev,f(k-1,0)+1);
		rev=min(rev,f(k-1,1)+1);
	}
	if(t==1 && flip(flip(k))==k && flip(k)<k)
		rev=min(rev,f(flip(k),0)+1);
	return rev;

}

int main(){

	int N;
	int T;

	cin >> T;

	SET(dn,-1);

	forn(i,1,1000000)
	{
		f(i,0);
		f(i,1);
		//cout <<  i << " " << min(f(i,0),f(i,1)) << endl;;
		//dbg(i);
	}

	forn(test,1,T){

		scanf(" %d",&N);

		//dbg(test);

		printf("Case #%d: %d\n",test,min(f(N,0),f(N,1)));

	}

	//cout << flip(N) << endl;

	//forn(i,1,N)
	//	printf("%d ",min(f(i,0),f(i,1)));

	return 0;
}

