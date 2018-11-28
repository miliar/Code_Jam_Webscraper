#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
const int N=10010;
int n,x;
int a[N];
int main()
{
    int T;
    int index=0;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    
	while(T--){
        index++;
        scanf("%d %d",&n,&x);
        for(int i=0;i<n;i++)scanf("%d",&a[i]);
		sort(a,a+n);
		int j=0;
		int count=0;
		for(int i=n-1;i>=0;i--)
		{
			if(i<=j)break;
			if(a[i]+a[j]<=x)j++,count++;
		}
        printf("Case #%d: %d",index,n-count);
        puts("");
    }
}
