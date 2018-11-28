#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int T;
int B,N;
int m[1005];
int a[1005];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    int t = 0;
    while(t < T)
    {
        cin>>B>>N;
        for(int i=0; i<B; i++)
        {
            scanf("%d",&m[i]);
        }
        long long l=0, r=100000000000000;
        long long mid,sum;
        int ans = 0;
        int kx = 0;
        while(1)
        {
            sum = 0;
            kx = 0;
            mid = (l + r) /2;
            for (int i=0;i<B; i++)
            {
                sum+= mid / m[i];
                if (mid % m[i] !=0 )
                {
                    sum++;
                }
                else
                {
                    kx++;
                    a[kx]=i+1;
                }
            }
            if (sum < N && kx+sum >= N)
            {
                ans = a[N-sum];
                break;
            }
            if (kx + sum < N)
            {
                l = mid+1;
            }else
            {
                r = mid-1;
            }
        }
        t++;
        printf("Case #%d: %d\n",t,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
