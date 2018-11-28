#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,i;
    long long int N,L,K;
    cin>>T;
    for(i=1;i<=T;++i)
    {
        int Arr[10]={0}, count1=0;
        cin>>N;
        if(N==0)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }

        for(K=N;true;K+=N)
        {
            L=K;
            while(L>0)
            {
                if(!Arr[L%10])
                {
                    Arr[L%10]++;
                    count1++;
                }
                L=L/10;
            }
            if(count1==10)
            {
                printf("Case #%d: %lld\n",i,K);
                break;
            }
        }

    }
    return 0;
}

