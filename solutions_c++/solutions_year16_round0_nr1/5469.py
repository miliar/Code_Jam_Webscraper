#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    int arr[10];

    for(int k=1;k<=tc;k++)
    {
        long long n;
        int g=0;
        memset(arr,0,sizeof(arr));
        long long x=1;
        long long temp;
        scanf("%lld",&n);
        temp = n;
        for(int i=1;i<=1000;i++)
        {
            int f=0;
            long long sum = x*n;
             x++;
             //cout<<temp<<endl;
             temp = sum;
            while(sum>0)
            {
                int r = sum%10;
                arr[r] = 1;
                sum/=10;
            }
            for(int i=0;i<10;i++)
            {
                //cout<<arr[i]<<" ";
                if(arr[i]==0)
                {
                    f=1;
                    break;
                }
            }
            //cout<<endl;

            if(f==0)
            {
                printf("Case #%d: %lld\n",k,temp);
                g=1;
                break;
            }


        }
        if(g==0)
        {
            printf("Case #%d: INSOMNIA\n",k);
        }
    }
    return 0;
}
