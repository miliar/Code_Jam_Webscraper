#include<bits/stdc++.h>
using namespace std;
long long freq[10];
long long arr[1000001];

bool check(long long num)
{
    while(num!=0)
    {
        freq[num%10]++;
        num/=10;
    }
    bool flag=true;
    for(long long i=0;i<10;i++) if(!freq[i]) flag=false;
    return flag;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long T,N,num;
    scanf("%I64d",&T);
    for(long long t=1;t<=T;t++)
    {
        scanf("%I64d",&N);
        if(N==0) printf("Case #%I64d: INSOMNIA",t);
        else
        {
            if(arr[N]!=0) printf("Case #%I64d: %I64d",t,arr[N]);
            else
            {
                for(long long j=0;j<10;j++) freq[j]=0;
                for(long long j=1; ;j++)
                {
                    num=j*N;
                    if(check(num))
                    {
                        arr[N]=num;
                        printf("Case #%I64d: %I64d",t,arr[N]);
                        break;
                    }
                }
            }
        }
        if(t!=T) printf("\n");
    }
    return 0;
}
