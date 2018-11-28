#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

int a[10050];
int main()
{
	freopen("1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int t,ti=1;scanf("%d",&t);
	while(t--)
    {
        int n;scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",a+i);
        int l=0,r=n-1,ans=0;
        for(int i=0;i<n;i++)
        {
            int f=a[l],pos=l;
            for(int j=l;j<=r;j++)
                if(a[j]<f)f=a[j],pos=j;
            ans+=min(pos-l,r-pos);
            if(pos-l>r-pos)
            {
                for(int j=pos;j<r;j++)
                    swap(a[j],a[j+1]);
                r--;
            }
            else
            {
                for(int j=pos;j>l;j--)
                    swap(a[j],a[j-1]);
                l++;
            }
        }
        printf("Case #%d: %d\n",ti++,ans);
    }
	return 0;
}
