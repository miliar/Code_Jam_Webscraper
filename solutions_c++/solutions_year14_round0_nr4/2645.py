#include<stdio.h>
#include<algorithm>
#define inf 1e9
#include<cstring>
using namespace std;
double na[2000],ke[2000];
int n;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,o=0,n,i,j;
	scanf("%d", &t );
	while ( t-- )
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%lf", &na[i]); 
		for(i=0;i<n;i++)
		scanf("%lf", &ke[i]);
		int ans=n;
		sort(na,na+n);
		sort(ke,ke+n); 
		printf("Case #%d: ",++o);
		j = 0;
		int an1=n,an2=0;
		for ( i = 0; i < n; i++ )
		{
			for (;j<n&&ke[j]<na[i];j++ );
			if ( j < n )
			an1--,j++;
		}
		j=n-1;
		int p = -1;
		for ( i = n-1;i>p&&j>=0;)
		{
			while ( j >= 0 && ke[j] > na[i] && p < i )
			p++,j--;
			if(j>=0&&ke[j]<na[i]&&p<i)
			i--,j--,an2++;
		}
		printf("%d %d\n",an2,an1);
	}
}
