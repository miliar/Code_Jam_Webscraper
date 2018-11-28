#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int t,count[17],c,v,i,j;
	int r1,r2,a[4][4],b[4][4];
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("jam1_out.txt","w",stdout);
	scanf("%d",&t);
	int q=1;
	while(t--){
		for(i=0;i<=16;i++) count[i]=0;
		scanf("%d",&r1);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++) scanf("%d",&a[i][j]);
		scanf("%d",&r2);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++) scanf("%d",&b[i][j]);
		for(j=0;j<4;j++) {
			count[a[r1-1][j]]++;
			count[b[r2-1][j]]++;
		}
		c=0; v=0;
		for(j=0;j<4;j++){
			if(count[a[r1-1][j]]>=2) {
				c++;
				v=a[r1-1][j];
			}
		}
		if(c==1) printf("Case #%d: %d\n",q,v);
		else if(c>=2) printf("Case #%d: Bad magician!\n",q);
		else printf("Case #%d: Volunteer cheated!\n",q);
		q++;
	}
	return 0;
}
