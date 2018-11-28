#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

double farm[100000],t[100000];
double C,F,X;
void find_sol()
{
	int i=1;
	double tmp;
	
	farm[0]=0;//買零座farm需要的時間
	t[0]=X/2;
	while(1)
	{
		farm[i]=farm[i-1]+C/(2+(i-1)*F);
		//total[i]=total[i-1]+farm[i];
		tmp=farm[i]+X/(2+i*F);
		t[i]=tmp>t[i-1]?t[i-1]:tmp;
		if(tmp>t[i-1])
			break;
		else
			i++;
	}
	printf("%.7f\n",t[i-1]);
}
int main()
{
	int T,i;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		memset(farm,0,sizeof(farm));//買n座farm需要的時間
		memset(t,0,sizeof(t));//有n座farm以後，所需要達成X的時間
		scanf("%lf %lf %lf",&C,&F,&X);
		printf("Case #%d: ",i);
		find_sol();
	}
	return 0;
}