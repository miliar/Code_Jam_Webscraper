#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
#define M 1000
using namespace std;
int f[M + 20][M + 20];
int a[M + 20];
int n;
void minimize(int &a,int b){
	if(a > b) a = b;
}
void prepare(){
	for(int from = 1 ; from <= M ; from++){
		for(int i = 1 ; i <= from ; i++)	f[from][i] = 0;
		for(int i = from + 1 ; i <= M ; i++){
			f[from][i] = 1e5;
			for(int j = 1 ; j < i ; j++)	minimize(f[from][i] , f[from][j] + f[from][i - j] + 1);
		}
	}
}
int solve(int from){
	int res = 0;
	for(int i = 1 ; i <= n ; i++) res+=f[from][a[i]];
	return res + from;
}
main(){
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	prepare();
	int T;
	scanf("%d",&T);
	for(int c = 1 ; c <= T ; c++){
		int curr = 2*M;
		scanf("%d",&n);
		for(int i = 1 ; i <= n ; i++)	scanf("%d",&a[i]);
		for(int i = 1 ; i <= M ; i++)	curr = min(curr , solve(i));
		printf("Case #%d: %d\n",c,curr);
	}
}
