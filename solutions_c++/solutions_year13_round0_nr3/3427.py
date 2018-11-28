#include<cstdio>
#include<cstdlib>
#include<cstring>
#define LI long long int

using namespace std;
int Y[1005];
int main(void)
{
	//FILE *in = fopen("in.txt","r");
	//FILE *out = fopen("out.txt","w");
	memset(Y,0,sizeof(Y));
	Y[1] = 1;
	Y[4] = 1;
	Y[9] = 1;
	Y[121] = 1;
	Y[484] = 1;
	int i,j,k;
	for(j=1;j<=1000;j++)
		Y[j] +=Y[j-1];
	int T;
	scanf("%d",&T);
	int A,B;
	for(i=1;i<=T;i++)
	{
		scanf("%d %d",&A,&B);
		printf("Case #%d: %d\n",i,Y[B]-Y[A-1]);
	}

	return 0;
}
