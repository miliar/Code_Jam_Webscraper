#include<bits/stdc++.h>
using namespace std;
#define sz 18

bool arr[sz];
int main()
{
    long long int tc,num,i,j,k,x,store;
    bool key;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%lld",&tc);
    for(k=1; k<=tc; k++)
    {
        scanf("%lld",&num);
        for(i=0; i<=99999; i++)
        {
            store=num*i;
            while(store)
            {
                arr[store%10]=true;
                store/=10;
            }
            key=true;
            for(j=0; j<=9; j++)
                if(!arr[j])
                {
                    key=0;
                    break;
                }
            if(key) break;
        }
        printf("Case #%d: ",k);
        if(key) printf("%lld\n",i*num);
        else printf("INSOMNIA\n");
        memset(arr,false,sizeof (arr));
    }
    return 0;
}
