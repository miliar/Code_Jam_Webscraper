#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

bool cmp(int a,int b)
{
	return a>b;
}

int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("A-small-attempt3.out","w",stdout);
	int n,m,max;
	int T,i,j,t;
	int a,b,c,d;
	int num[20];
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		memset(num,0,sizeof(num));
		for(i=1;i<=4;i++){
			if(i==n){
				for(j=0;j<4;j++){
					scanf("%d",&a);	
					num[a]++;
				}
			} else {
				scanf("%d%d%d%d",&a,&d,&d,&d);
			}
		}
		max=0;
		scanf("%d",&m);
		for(i=1;i<=4;i++){
			if(i==m){
				for(j=0;j<4;j++){
					scanf("%d",&a);
					num[a]++;
					if(num[a]>num[max]){
						max=a;
					}		
				}
			} else {
				scanf("%d%d%d%d",&a,&d,&d,&d);
			}
		}
		sort(num,num+17,cmp);
		printf("Case #%d: ",t);
		if(num[0]==1){
			printf("Volunteer cheated!\n");
		} else if(num[0]==2 && num[1]==1){
			printf("%d\n",max);
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}