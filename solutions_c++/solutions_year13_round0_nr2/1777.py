/// @file
/// @brief	문제: 
///	해결법 : 
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<algorithm>
#include<cassert>
#include<cctype>
using namespace std;

#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,n) for (int (i)=0,_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b) for (int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset((x),0,sizeof(x));
#define CLEARA(x) memset(&(x),0,sizeof(x));
#define FILL(x,v) memset((x),(v),sizeof(x));
#define FILLA(x,v) memset(&(x),(v),sizeof(x));

//c++ 0x
#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define rFOREACH(it,c) for(auto it=(c).rbegin();it!=(c).rend();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
//const double pi = acos(-1.0);
#define EPS 1e-9

#define PII pair<int,int> 
#define VI vector<int>
#define LL long long
template<typename T> inline T		gcd(T a, T b){if(a>b)swap(a,b);while(a!=0){b%=a;swap(a,b);}return b;}
template<typename T> inline T		lcm(T a, T b){return a/gcd(a,b)*b;}
//int pow(int a,int b){int c=1;while(b--)c*=a;return c;}


//#define PROB   "d:\\B-small-attempt3"
#define PROB   "d:\\B-large"

int row,col,height[100][100];
bool isVisit[100][100];
bool isPossible[100][100];
int cnt;

void FloodFill(int r,int c,int h)
{
	if(r<0 || r>=row || c<0 || c>=col)return;
	if(isVisit[r][c] && isPossible[r][c])return;
	isVisit[r][c]=true;
	if(h<=height[r][c]){
		isPossible[r][c]=true;
		cnt++;
		FloodFill(r-1,c,height[r][c]);
		FloodFill(r+1,c,height[r][c]);
		FloodFill(r,c-1,height[r][c]);
		FloodFill(r,c+1,height[r][c]);
	}
}

int main(){
	freopen(PROB ".in","r",stdin);
	freopen(PROB ".out","w",stdout);

	int maxRow[100],maxCol[100],maxVal;
	int board[100][100];
	int T;scanf("%d",&T);
	FOR(t,1,T){
		scanf("%d %d",&row,&col);
		FILL(maxRow,-1);
		FILL(maxCol,-1);
		rep(r,row)rep(c,col){
			scanf("%d",&height[r][c]);
			maxRow[r]=max(maxRow[r],height[r][c]);
			maxCol[c]=max(maxCol[c],height[r][c]);
		}
		FILL(board,0x7f);
		bool res=true;
		//Cutting From Edge to go another Edge
		rep(r,row)rep(c,col){
			if(height[r][c]!=maxRow[r] && height[r][c]!= maxCol[c])
			{res=false;goto Print;}
		}
Print:
		fprintf(stderr,"Case #%d: %s\n",t,res?"YES":"NO");
		printf("Case #%d: %s\n",t,res?"YES":"NO");
	}
	fclose(stdout);
	return 0;
}