#include<bits/stdc++.h>
using namespace std;
#define maxn 10000

double A[maxn],B[maxn];

bool cmp(double a,double b)
{
    return a>b;
}

int gao1(int n)
{
    int ans=0,i,j;
	j=0;
	for(i=0;i<n;i++)
	{
	    while(B[i]<A[j]&&j<n)
		    j++;
		if(j==n)
		    break;
		ans++;
		j++;
	}
	return n-ans;
}
int gao2(int n)
{
    int ans=0,i,j;
	j=0;
	for(i=0;i<n;i++)
	{
	    while(A[i]<B[j]&&j<n)
		    j++;
		if(j==n)
		    break;
		ans++;
		j++;
	}
	return ans;
}
int main()
{
    int casen,T,n,i,ans1,ans2;
	scanf("%d",&T);
	for(casen=0;casen<T;casen++)
	{
	    scanf("%d",&n);
	    for(i=0;i<n;i++)
	       scanf("%lf",A+i);
		for(i=0;i<n;i++)
           scanf("%lf",B+i);
        sort(A,A+n,cmp);
        sort(B,B+n,cmp);
		ans1=gao1(n);
		ans2=gao2(n);
		printf("Case #%d: %d %d\n",casen+1,ans2,ans1);
    }		
    return 0;
}