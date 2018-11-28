#include <iostream>
#include <cstdio>
#include <cstring>
#define N 5
#define rep(i,l,r) for (int i = l;i <= r;i ++)
using namespace std;

int mat[N][N];
bool vis[20];

void init(){
	memset(vis,false,sizeof(vis));
}

int main (){
	int cas,T = 0;
	freopen ("a.in","r",stdin);
	freopen ("a.txt","w",stdout);
	cin >> cas;
	while (cas --){
		int t;
		init();
		scanf ("%d",&t);
		rep(i,1,N - 1)
			rep(j,1,N - 1) scanf ("%d",&mat[i][j]);
		rep(i,1,N - 1) vis[mat[t][i]] = true;
		cin >> t;
		int res = 0;
		int flag;
		rep(i,1,N - 1)
			rep(j,1,N - 1)
				scanf ("%d",&mat[i][j]);
		rep(i,1,N - 1) 
			if (vis[mat[t][i]]){
				res ++;
				flag = mat[t][i];
			}
		printf ("Case #%d: ",++ T);
		if (res == 0) puts ("Volunteer cheated!");
		else if (res == 1) printf ("%d\n",flag);
		else puts ("Bad magician!");

	}
	return 0;
}
