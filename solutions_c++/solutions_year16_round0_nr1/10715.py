#include<bits/stdc++.h>
using namespace std;
int A[12];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    cin>>t;
    int k=0;
    int x;

    while(t--)
    {
        scanf("%d",&x);
        int cnt=0;
        memset(A,0,sizeof(A));
        if(x==0)
            printf("Case #%d: INSOMNIA\n",++k);

        else
        {
            int tmp;
            tmp=x;
            int tmp1;
            int ans=0;
            while(1)
            {
                tmp1=tmp;
                while(tmp)
                {
                    if(!A[tmp%10])
                    {
                        A[tmp%10]=1;
                        cnt++;
                    }
                    tmp/=10;
                }
                ans++;
                if(cnt>=10)
                    break;
                tmp=tmp1+x;
            }
            printf("Case #%d: %d\n",++k,tmp1);
        }
    }
    return 0;
}
