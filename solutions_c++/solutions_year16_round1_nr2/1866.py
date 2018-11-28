#include<bits/stdc++.h>

using namespace std;

#define std::cout cout;
#define std::cin cin;

int main()
{
	int i,j,t,cases;
	int n[50][50],N,comp[2500],arr[2500],s;
	freopen("problem2 large.in","r",stdin);
    freopen("problem2 large.out","w",stdout);
    scanf("%d",&cases);
    for(t=1;t<=cases;t++)
    {
    scanf("%d",&N);
    for(i=0;i<2500;i++)
    {
        comp[i]=0;
    }
    for(i=1;i<=((2*N)-1);i++)
    {
        for(j=1;j<=N;j++)
        {
            scanf("%d",&s);
            comp[s-1]++;
        }
    }
    printf("Case #%d: ",t);
    for(i=0;i<2500;i++)
    {
        if(comp[i]%2!=0 && comp[i]!=0)
        {
            printf("%d ",i+1);
        }
    }
    printf("\n");
    }
	return 0;
}
