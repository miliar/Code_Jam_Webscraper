#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#define CL(x,y) memset(x,y,sizeof(x))
#define pb(x) push_back(x)
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(e);i++)
#define x first
#define y second
#define MAX 10005
#define INF 1<<29

using namespace std;

int T,TC,n;
bool v[10];

bool ok(){
	for (int i=0;i<10;i++) if (!v[i]) return false;
	return true;
}

int main(){
	scanf("%d",&T);
	while (T--){
		CL(v,0);
		scanf("%d",&n);
		printf("Case #%d: ",++TC);
		if (n==0) {printf("INSOMNIA\n"); continue;}
		for (int i=1;;i++){
			int t=i*n;
			while (t>0){
				v[t%10]=true;
				t/=10;
			}
			if (ok()) {
				printf("%d\n",i*n);
				break;
			}
		}
	}
}
