//counting sheep.cpp
#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

#define all(c) c.begin(),c.end()

int v[10]={0,0,0,0,0,0,0,0,0,0};

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int loop,temp,t,j,ct,index;
    long long int n,n_copy,nts;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%lld",&n);
        ct=1;
        while(ct)
        {
            if(n==0)
            {
                printf("Case #%d: INSOMNIA\n",j );
                break;
            }
            else
            {
                n_copy=n;
                n_copy*=ct;
                nts=n_copy;
                while(n_copy)
                {
                    index=(n_copy%10);
                    v[index]++;
                    n_copy/=10;
                }
                if((*(min_element(v,v+10))) != 0 )
                {
                    printf("Case #%d: %lld\n",j,nts );
                    break;
                }
                ct++;
            }
        }
        for(loop=0;loop<10;loop++)
            v[loop]=0;
    }

    return 0;
}
