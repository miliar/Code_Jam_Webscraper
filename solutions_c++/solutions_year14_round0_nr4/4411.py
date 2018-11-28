#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;
double a[1010],b[1010];
int map[1010],fans,n;
bool exist[1010];
void out()
{
	int r=n-1,l=0;
	int ans=0;
	/*for(int i=1;i<=n;i++)
	{
		if(a[map[i]]<b[r])
		{
            r--;
			continue;
		}
		ans++;
		l++;
	}*/
	for(int i=1;i<=n;i++)
    {
        if(a[map[i]]<b[r])
        {
            r--;
            continue;
        }
        ans++;
        r--;
    }

	if(ans>fans)fans=ans;
}
void search(int t)
{
	if(t>n){out();return;}
	for(int i=0;i<n;i++)
		if(exist[i])
		{
			map[t]=i;
			exist[i]=0;
			search(t+1);
			exist[i]=1;
		}
}
void worka()
{

    /*for(int i=0;i<n;i++)
    {
        if(a[i]<b[r])
        {
            r--;
            continue;
        }
        ans++;
        r--;
    }*/
    int ra=n-1,rb=n-1,la=0,lb=0,ans=0;
    for(int i=0;i<n;i++)
    {
        if(a[ra]>b[rb])
        {
            ans++;
            ra--;
            rb--;
            continue;
        }
        la++;rb--;
    }
    fans=ans;
}
void work()
{
    int k=0,ans=0;
    for(int i=0;i<n;i++)
    {
        while(a[i]>b[k] && k<n)k++;
        if(b[k]>a[i])
        {
            ans++;
            k++;
        }
    }
    fans=n-ans;

}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("d2.out","w",stdout);
	int T,Case=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		fans=0;
		memset(exist,1,sizeof(exist));
		worka();
		printf("Case #%d: %d ",++Case,fans);
        work();
        printf("%d\n",fans);
	}
	return 0;
}
