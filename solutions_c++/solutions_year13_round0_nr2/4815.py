#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <climits>
#include <ctime>

#define pb       	push_back
#define fi       	first
#define se       	second
#define KARE(a)	 	( (a)*(a) )
#define MAX3(a,b,c)	( MAX( a,MAX(b,c) ) )
#define inf		 	1000000000
#define eps      	(1e-9)
#define esit(a,b)  	( abs( (a)-(b) ) < eps )
#define SET(A,b) memset(A,b,sizeof (A) )
#define SIZE(A) ((int)(A).size())
#define yeral() (node *)calloc(1,sizeof(node))
#define dbg(x) cerr<<#x<<":"<<x<<endl

using namespace std;

typedef long long int lint;
typedef pair<int,int> ii;

char word[][5]={"YES","NO"};
int T,N,M,mat[105][105],row[105],col[105];
int main()
{
	freopen("oku.txt","r",stdin);
	freopen("yaz.txt","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d %d",&N,&M);
		SET(row,0);
		SET(col,0);
		for(int i=1;i<=N;i++)
			for(int j=1;j<=M;j++)
				scanf("%d",&mat[i][j]);
		for(int i=1;i<=N;i++)
			for(int j=1;j<=M;j++)
				row[i]=max(row[i],mat[i][j]);
		for(int i=1;i<=M;i++)
			for(int j=1;j<=N;j++)
				col[i]=max(col[i],mat[j][i]);
		int fl=0;
		for(int i=1;i<=N;i++)
			for(int j=1;j<=M;j++)
				if(mat[i][j]<row[i] && mat[i][j]<col[j]) 	
					fl=1;
		
		printf("Case #%d: %s\n",tt,word[fl]);
	}
	
}

