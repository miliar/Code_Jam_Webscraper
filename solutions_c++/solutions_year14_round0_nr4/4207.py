#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int T,t,n;
double x[1010],y[1010];
int ans1,ans2;

int main()
{
    int i,j;
    freopen("Din.in","r",stdin);
    freopen("Dout.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++) scanf("%lf",&x[i]);
        for(i=1;i<=n;i++) scanf("%lf",&y[i]);
        sort(x+1,x+1+n);
        sort(y+1,y+1+n);

        ans1=ans2=0;
        for(i=n,j=n;i>=1;i--)
        {
            while(j>0&&x[i]<y[j]) j--;
            if(j==0) break;
            j--;
            ans1++;
        }
        for(i=n,j=n;i>=1;i--)
        {
            while(j>0&&y[i]<x[j]) j--;
            if(j==0) break;
            j--;
            ans2++;
        }
        printf("Case #%d: %d %d\n",t,ans1,n-ans2);
    }
    return 0;
}
/*
4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458

Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4
*/
