#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int T;cin>>T;
    for(int cases=1;cases<=T;cases++)
    {
        int a,b,k;
        scanf("%d %d %d",&a,&b,&k);
        int ans=0;
        for(int i=0;i<a;i++)
            for(int j=0;j<b;j++)
            {
                if((i&j) < k)    ans++;
                //cout<<i<<"  "<<j<<" "<<(i&j)<<endl;
            }
        printf("Case #%d: %d\n",cases,ans);
    }    
    return 0;
}