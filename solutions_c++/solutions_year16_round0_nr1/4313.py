#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.o", "w", stdout);
    set<int>s;
    int t;
    long long i,j,k,p;
    scanf("%d",&t);
    for(i=1; i<=t; i++)
    {
        s.clear();
        scanf("%lld",&p);
        j=1;
        printf("Case #%d: ",i);
        if(p==0)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            while(s.size()!=10)
            {
                k=j*p;
                while(k!=0)
                {
                    s.insert(k%10);
                    k/=10;
                }
                j++;
            }
            printf("%lld\n",(j-1)*p);
        }
        s.clear();
    }

}
