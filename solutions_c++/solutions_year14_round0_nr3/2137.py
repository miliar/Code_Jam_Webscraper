#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>

#define FOR(a,b,c) for(int (a)=(b);(a)<=(c);(a)++)
#define TFOR(a,b,c) for(int (a)=(b);(a)>=(c);(a)--)
#define SET(A,b) memset(A,b,sizeof (A) )
#define SIZE(A) ((int)(A).size())
#define fi first
#define se second
#define num(a) (1<<(a))
using namespace std;

typedef pair<int,int> ii;

int cnt_bit(int k){
	int x=0;
	FOR( i,0,26 )
		if( num(i)&k )
			x++;
	return x;
}
int T,R,C,M;
int dir[8][2]={{0,1},{0,-1},{1,0},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
int used[10][10];
int kont(int k){
	
	int tbl[55][55];
	
	FOR(i,0,R-1)
		FOR(j,0,C-1)
			tbl[i][j]=( num( (i*C+j) )&k )>0;
	
	ii beg=ii(-1,-1);
	
	FOR(i,0,R-1)
		FOR(j,0,C-1)
			if(tbl[i][j]==0)
			{
				int cnt=0;
				FOR(t,0,7)
					if( i+dir[t][0]>=0 && i+dir[t][0]<R && j+dir[t][1]>=0 && j+dir[t][1]<C )
						cnt+=tbl[i+dir[t][0]][j+dir[t][1]];
				
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
		FOR(t,0,7)
			if( tmp.fi+dir[t][0]>=0 && tmp.fi+dir[t][0]<R && tmp.se+dir[t][1]>=0 && tmp.se+dir[t][1]<C )
				cnt+=tbl[tmp.fi+dir[t][0]][tmp.se+dir[t][1]];
		if(cnt)	continue;
		FOR(t,0,7)
			if( tmp.fi+dir[t][0]>=0 && tmp.fi+dir[t][0]<R && tmp.se+dir[t][1]>=0 && tmp.se+dir[t][1]<C )
				if(!used[ tmp.fi+dir[t][0] ][ tmp.se+dir[t][1] ])
					used[ tmp.fi+dir[t][0] ][ tmp.se+dir[t][1] ]=1,q.push(ii( tmp.fi+dir[t][0] , tmp.se+dir[t][1] ));
		
	}
	
	if(say+M==R*C){
		FOR(i,0,R-1){
			FOR(j,0,C-1)
				if(i==beg.fi && j==beg.se)
					printf("c");
				else if( tbl[i][j] )
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
	
	FOR(test,1,T){
		scanf(" %d %d %d",&R,&C,&M);
		printf("Case #%d:\n",test);
		FOR( i,0,num(R*C)-1 ){
			if(cnt_bit(i)!=M)	continue;
			if( kont(i) )
				goto END;
			
		}
		printf("Impossible\n");
		END:;
	}
	
	return 0;
	
}
