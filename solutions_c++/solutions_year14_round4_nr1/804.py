#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int a[10050];
int main()
{
	freopen("1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int t,ti=1;scanf("%d",&t);
	while(t--)
    {
        int n,x;scanf("%d%d",&n,&x);
        for(int i=0;i<n;i++)
            scanf("%d",a+i);
        sort(a,a+n);
        int p=0,tot=0;
        for(int i=n-1;i>=p;i--)
        {
            if(a[p]+a[i]<=x)p++;
            tot++;
        }
        printf("Case #%d: %d\n",ti++,tot);
    }
	return 0;
}
