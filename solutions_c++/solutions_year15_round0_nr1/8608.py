
#include<stdio.h>
int main(){
	freopen("small.in", "r", stdin);
	freopen("small.txt", "w", stdout);
	int a,i,j;
	int sum=0;
	char str[1000][1000];
	int p[1000],c[1000]={0};
	scanf("%d",&a);
	for(i=0;i<a;i++)
		{
		scanf("%d %s",&p[i] , str[i]);
	}
	for(i=0;i<a;i++)
		{
		//	sum=0;
		sum=str[i][0]-'0';
		for(j=1;j<p[i]+1;j++)
			{
			//printf("%d-sum(%d)",sum,j);
			if(sum<j) {
			c[i]=c[i]+j-sum;
			sum=j+str[i][j]-'0';
			}
			else sum =sum+str[i][j]-'0';
			}
			//if(c[i]<0) c[i]=0;
		printf("Case #%d: %d\n",i+1,c[i]);
	}
	return 0;
}
