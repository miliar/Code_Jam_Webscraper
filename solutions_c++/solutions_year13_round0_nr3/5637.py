#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#define INF 2000000000
#define x first
#define y second
using namespace std;

int T;
int A,B;
int List[] = {1,4,9,121,484,10000000};

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int k=1;k<=T;k++){
		int countt = 0;
		scanf("%d%d",&A,&B);
		for(int i=0;i<6;i++){
			if(A<=List[i] && List[i]<=B){
				countt++;
			}
		}
		printf("Case #%d: %d\n",k,countt);
	}
}
