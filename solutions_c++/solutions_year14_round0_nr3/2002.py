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
#define num(a) (1<<(a))
using namespace std;

typedef double dbl;
typedef long long Lint;
typedef pair<int,int> ii;
typedef pair<Lint,Lint> Lii;

const Lint mod = 1e9;

const int MAXN = 200010;

int count(int k){
	
	int cnt=0;
	
	forn(i,0,26)
		if(num(i)&k)
			cnt++;
	return cnt;
	
}

int T,R,C,M;

int yon[8][2]={{0,1},{0,-1},{1,0},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};

int used[10][10];

int kont(int k){
	
	int ar[55][55];
	
	forn(i,0,R-1)
		forn(j,0,C-1)
			ar[i][j]=( num( (i*C+j) )&k )>0;
	
	ii beg=ii(-1,-1);
	
	forn(i,0,R-1)
		forn(j,0,C-1)
			if(ar[i][j]==0)
			{
				int cnt=0;
				forn(t,0,7)
					if( i+yon[t][0]>=0 && i+yon[t][0]<R && j+yon[t][1]>=0 && j+yon[t][1]<C )
						cnt+=ar[i+yon[t][0]][j+yon[t][1]];
				
				if(cnt==0 || M==R*C-1){
					beg=ii(i,j);
					goto Next;
				}
			}
	Next:;
	
	queue<ii> q;
	q.push(beg);
	
	SET(used,0);
	
	if(beg.fi==-1) return 0;
	
	used[beg.fi][beg.se]=1;
	int cnt=0,say=0;
	ii tmp;
	while( !q.empty() ){
		say++;
		tmp=q.front();
		q.pop();
		cnt=0;
		forn(t,0,7)
			if( tmp.fi+yon[t][0]>=0 && tmp.fi+yon[t][0]<R && tmp.se+yon[t][1]>=0 && tmp.se+yon[t][1]<C )
				cnt+=ar[tmp.fi+yon[t][0]][tmp.se+yon[t][1]];
		//~ printf ("%d %d -> %d\n",tmp.fi,tmp.se,cnt);
		if(cnt)	continue;
		//~ printf ("%d %d -> %d\n",tmp.fi,tmp.se,cnt);
		forn(t,0,7)
		{
			//~ printf("%d %d -> %d %d\n",tmp.fi,tmp.se,tmp.fi+yon[t][0],tmp.se+yon[t][1]);
			if( tmp.fi+yon[t][0]>=0 && tmp.fi+yon[t][0]<R && tmp.se+yon[t][1]>=0 && tmp.se+yon[t][1]<C )
			{
				//~ printf("%d %d -> %d %d\n",tmp.fi,tmp.se,tmp.fi+yon[t][0],tmp.se+yon[t][1]);
				if(!used[ tmp.fi+yon[t][0] ][ tmp.se+yon[t][1] ])
					used[ tmp.fi+yon[t][0] ][ tmp.se+yon[t][1] ]=1,q.push(ii( tmp.fi+yon[t][0] , tmp.se+yon[t][1] ));
			}
		}
		
	}
	
	if(say+M==R*C){
		
		forn(i,0,R-1){
			forn(j,0,C-1)
				if(i==beg.fi && j==beg.se)
					printf("c");
				else if( ar[i][j] )
					printf("*");
				else
					printf(".");
			printf("\n");
		}
		return 1;
	}
	else
		return 0;
	
}

int main(){
	
	scanf(" %d",&T);
	
	forn(test,1,T){
		
		//dbg(test);
		
		scanf(" %d %d %d",&R,&C,&M);
		
		printf("Case #%d:\n",test);
		
		forn( i,0,num(R*C)-1 ){
			
			if(count(i)!=M)	continue;
			
			if( kont(i) )
				goto END;
			
		}
		
		printf("Impossible\n");
		
		END:;
	}
	
	return 0;
	
}
