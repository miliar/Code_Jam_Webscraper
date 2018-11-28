#include<cstdio>
#include<iostream>
using namespace std;
int T,D;
int a[1006];
int b[1006];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    int t = 0;
    while(t < T)
    {
        cin>>D;
        for (int i=0;i<1006;i++) b[i]=0;
        int maxn = 0;
        for (int i=1;i<=D;i++)
        {
            scanf("%d",&a[i]);
            b[a[i]]++;
            if (maxn<a[i]) maxn = a[i];
        }
        int ans = maxn;
        for (int i=1; i<maxn; i++)
        {
            int sum = 0;
            for(int j=i+1;j<=maxn;j++)
            {
                if (b[j] > 0)
                {
                    sum += (j/i)*b[j];
                    if (j%i) sum += b[j];
                    sum -= b[j];
                }
            }
            if (sum+i<ans) ans = sum+i;
        }
        t++;
        printf("Case #%d: ",t);
        cout<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
