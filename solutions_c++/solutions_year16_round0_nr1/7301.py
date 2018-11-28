#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
   long long int t,n,c=1,cnt,p,k,q;

    int a[10];

    cin>>t;

    while(t--)
    {
        cin>>n;
        cnt=0;
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",c);
            c++;
        }
        else
        {
            p=n;
            k=2;

            memset(a,-1,sizeof(a));

            while(1)
            {
                q=p%10;
                p=p/10;

                if(a[q]==-1)
                {
                    a[q]=1;
                    cnt++;
                }
                         if(cnt==10) break;
                if(p==0)
                {
                    p=k*n;
                    k++;

                }

            }
            printf("Case #%lld: %lld\n",c,(k-1)*n);
            c++;
        }
    }
}
