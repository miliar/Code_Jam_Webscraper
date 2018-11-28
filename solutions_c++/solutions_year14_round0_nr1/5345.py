#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
//int max(int x,int y){ return x>=y?x:y; }
//int min(int x,int y){ return x<=y?x:y; }
int main()
{
int N;
scanf("%d",&N);
for(int T=1;T<=N;T++)
{
	int b1[4][4],b2[4][4],b3[17]={0};
	int r,c;
	scanf("%d",&r); r--;
	for(int a=0;a<4;a++) for(int s=0;s<4;s++) scanf("%d",&b1[a][s]);
	scanf("%d",&c); c--;
	for(int a=0;a<4;a++) for(int s=0;s<4;s++) scanf("%d",&b2[a][s]);
	for(int s=0;s<4;s++) b3[b1[r][s]]++;
	for(int s=0;s<4;s++) b3[b2[c][s]]++;
	int o=-1;
	printf("Case #%d: ",T);
	for(int d=1;d<=16;d++) if( b3[d]==2 ) if( o!=-1 ){ printf("Bad magician!"); goto done; } else o=d;
	if( o==-1 ) printf("Volunteer cheated!");
	else printf("%d",o);
done:;
	printf("\n");
}
	return 0;
}
