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

const Lint mod = 1e9+7;


const int MAXN = 210;

vector<int> v;

int N,J;

bool isDivide(int b,Lint k,int m){
	Lint cur = 1LL;
	Lint tot = 0LL;
	while(k){
		if(k&1)
			tot=(tot+cur)%m;
		cur = (cur*b)%m;
		k>>=1;
	}
	if(tot)	return false;
	return true;
}

bool isComp(int b,Lint k){

	forn(i,2,500)
		if( isDivide(b,k,i) )
		{
			v.pb(i);
			return true;
		}
	return false;

}

bool check(Lint k){
	k<<=1;
	k|=1;
	k|=1LL<<(N-1);
	v.clear();
	forn(j,2,10)
	{
		if(!isComp(j,k))
			return false;
	}
	return true;
}

void print(Lint k){
	k<<=1;
	k|=1;
	k|=1LL<<(N-1);
	forr(i,(N-1),0){
		if(k&(1LL<<i))
			cout << 1;
		else
			cout << 0;
	}
	cout << " ";
	forn(i,0,SIZE(v)-1){
		printf("%d ",v[i]);
	}
	puts("");
}

int main(){

	int T;
	scanf(" %d",&T);
	scanf("%d %d",&N,&J);

	printf("Case #1:\n");
	for(int i=0;J;i++){
		if( check(i) ){
			print(i);
			J--;
		}
	}
	return 0;
}