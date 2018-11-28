// Task-ID: 1395
#include <algorithm>
#include <iterator>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <ctime>
#include <cmath>
#include <list>
#include <map>
#include <set>

#define maxn 1010
#define pb push_back
#define fi first
#define se second
#define all(x) x.begin(),x.end()
#define fill(x,y) memset((x),(y) ,sizeof(x))
#define type(x) __typeof(x.begin())
#define sz(x) x.size()
#define o ((f+l)/2)
#define umax(x,y) (x)=max((x),(y))
#define NEW(x) (x *)calloc(1,sizeof(x))
#define umin(x,y) (x)=min((x),(y));
#define tmax(x,y,z) max((x),max((y),(z))) 
#define tmin(x,y,z) min((x),min((y),(z))) 
#define PI (acos(-1)) 

using namespace std;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef long long int Lint;

int A,B,K,T;
Lint res=0;

int main ()
{
	
	scanf("%d",&T);
	for( int h=1 ; h<=T ; h++ ){
		res=0;
		scanf("%d %d %d",&A,&B,&K);
		for( int i=0 ; i<A ; i++ )
			for( int j=0 ; j<B ; j++ )  
				if( (i&j)<K )
					res++;
		printf("Case #%d: %lld\n",h,res);
	}
				
	
	return 0;
}
