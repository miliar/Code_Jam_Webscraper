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

#define maxn 110
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

int T,N,deg[maxn][maxn];
char er[maxn][maxn];	

int main ()
{
	scanf("%d",&T);
	
	for( int t=1 ; t<=T ; t++ ){
		
		for( int i=1 ; i<=N ; i++ )
			for( int j=1 ; er[i][j] ; j++ ){
				er[i][j]='\0';
				deg[i][j]=0;
			}
		
		scanf("%d",&N);
		vector<char > we[maxn];
		for( int i=1 ; i<=N ; i++ )
			scanf("%s",er[i]+1);
		int flag=0;
		for( int i=1,k=0 ; i<=N ; i++,k=0 ){
			for( int j=1 ; er[i][j] ; j++ ){
				if( er[i][j]!=er[i][j-1] ){
					we[i].pb( er[i][j] ) ;
					k++;
				}
				else 
					deg[i][k]++;
			}
			if( we[i]!=we[1] ){
				flag=1;
				break;
			}
		}
		
		if( flag ){
			printf("Case #%d: Fegla Won\n",t);
			continue;
		}
		
		
		Lint sum=0,res=0;
		for( int i=1 ; i<=(int)sz(we[1]) ; i++ ){
			sum=0;
			for( int j=1 ; j<=N ; j++ )
				sum+=deg[j][i];
			sum/=N;
			for( int j=1 ; j<=N ; j++ )
				res+=abs( deg[j][i]-sum );
		}
		printf("Case #%d: %lld\n",t,res);
	}
	
	return 0;
}
	
