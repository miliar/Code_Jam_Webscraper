#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;
int a[10001];
int comp(const void *a,const void *b)
	{
	return (*(int *)a)-(*(int *)b);
	}
int main()
{
int T;
long long i,h,j,k;
//long long a,b,c;
freopen("i1.txt","r",stdin);
freopen("o1.txt","w",stdout);

scanf("%d",&T);

int n,x;
for(int t=0;t<T;t++)
	{
	scanf("%d %d",&n,&x);
	for(j=0;j<n;j++)
		scanf("%d",&a[j]);
	qsort(a,n,sizeof(int),comp);
	i=0;
	j=n-1;
	k=0;
	while(i<=j)
		{
		if(a[i]+a[j]>x)
			{
			k++;
			j--;
			continue;
			}
		k++;
		i++;
		j--;
		}
	printf("Case #%d: %lld\n",t+1,k);	
	}
return 0;
}
