#include<stdio.h>
#include<algorithm>
using namespace std;
double l[1004],g[1004];int n;
int main()
{
    int zes;scanf("%d",&zes);
    for (int k=0;k<zes;k++)
    {
	scanf("%d",&n);
	for (int i=0;i<n;i++)
	{
	    scanf("%lf",&l[i]);
	}
	for (int i=0;i<n;i++)
	    scanf("%lf",&g[i]);
	sort(l,l+n);sort(g,g+n);
	int resg=0,res2=0;
	int j=0;
	for (int i=0;i<n;i++)
	{
	    while(g[j]<l[i] && j<n-1)
		j++;
	    if(g[j]>l[i]) resg++;	
	    if(j==n-1) break;
	    j++;
	}
	int res1=n-resg;
	j=0;
	for (int i=0;i<n;i++)
	{
	    while(l[j]<g[i] && j<n-1)
		j++;
	    if(l[j]>g[i]) res2++;
	    if(j==n-1) break;
	    j++;
	}
	

	printf("Case #%d: %d %d\n",k+1,res2,res1);
    }
}

