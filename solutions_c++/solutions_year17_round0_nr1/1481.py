#include <cstdio>
#include <cstring>

using namespace std;

const int Maxn=1000;
int n,k;
char str[Maxn+5];

inline void solve(int T){
	scanf("%s%d",str+1,&k);
	n=strlen(str+1);

	int Ans=0;
	for (int i=1;i<=n && Ans!=-1;i++){
		if (str[i]=='-'){
			if (i+k-1>n){
				Ans=-1;
				break;
			}
			for (int j=i;j<=i+k-1;j++) if (str[j]=='-') str[j]='+'; else str[j]='-';
			Ans++;
		}
	}

	printf("Case #%d: ",T);
	if (Ans==-1) printf("IMPOSSIBLE\n"); else printf("%d\n",Ans);
}

int main(){
	freopen("A-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T=0;
	scanf("%d",&T);
	for (int i=1;i<=T;i++) solve(i);
	return 0;
}