#include<cstdio>
#include<cstring>
#include<algorithm>
#define maxn (10005)
using namespace std;

int test,N,X,A[maxn];
bool vis[maxn];

int main(){
	freopen("i.txt","r",stdin);
	scanf("%d",&test);
	for (int testcase=1;test--;testcase++){
		printf("Case #%d: ",testcase);
		scanf("%d%d",&N,&X);
		for (int i=0;i<N;i++) scanf("%d",&A[i]);
		sort(A,A+N);
		memset(vis,0,sizeof(vis));
		int res=0;
		/*int i=0,j=N-1;
		for (;j>=0;j--){
			if (vis[j]) continue;
			vis[j]=true;
			res++;
			if (i>=j){
				for (;i>=0 && vis[i];i--);
				if (i>=0 && A[i]+A[j]<=X){
					vis[i]=true;
					//printf("%d %d\n",A[i],A[j]);
				}
			}
			else{
				for (;i+1<j && A[i+1]+A[j]<=X;i++);
				if (A[i]+A[j]<=X){
					//printf("%d %d\n",A[i],A[j]);
					vis[i++]=true;
				}
			}
		}*/
		for (int j=N-1;j>=0;j--){
			if (vis[j]) continue;
			vis[j]=true;
			res++;
			for (int i=j-1;i>=0;i--) if (!vis[i] && A[i]+A[j]<=X){
				vis[i]=true;
				break;
			}
		}
		printf("%d\n",res);
	}
	return 0;
}
