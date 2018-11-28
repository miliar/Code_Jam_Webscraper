#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int MAX=110;
int b[MAX][MAX],l[MAX][MAX];
struct Node{
	int y,x;
	int val;
	Node(){}
	Node(int yi,int xi,int vali){y=yi;x=xi;val=vali;}
}p[MAX*MAX];

bool comp(Node a,Node bb){
	return a.val>bb.val;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int n,m,t,i,j,k,tc;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++){
		scanf("%d%d",&n,&m);
		k=0;
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				scanf("%d",&l[i][j]);
				p[k++]=Node(i,j,l[i][j]);
			}
		}
		sort(p,p+k,comp);
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				b[i][j]=100;
			}
		}
		for(i=0;i<k;i++){
			if(b[p[i].y][p[i].x]>l[p[i].y][p[i].x]){
				for(j=1;j<=n;j++){
					if(l[j][p[i].x]>l[p[i].y][p[i].x])break;
				}
				if(j==n+1){
					for(j=1;j<=n;j++){
						b[j][p[i].x]=l[p[i].y][p[i].x];
					}
					continue;
				}
				for(j=1;j<=m;j++){
					if(l[p[i].y][j]>l[p[i].y][p[i].x])break;
				}
				if(j==m+1){
					for(j=1;j<=m;j++){
						b[p[i].y][j]=l[p[i].y][p[i].x];
					}
				}else{
					break;
				}
			}
		}
		printf("Case #%d: ",tc);
		if(i==k)printf("YES\n");
		else printf("NO\n");
	}
    return 0;
}
