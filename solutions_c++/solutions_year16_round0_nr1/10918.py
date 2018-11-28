#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    long cs,tst;
    scanf("%lld",&cs);
    for(tst=1;tst<=cs;tst++)
    {
        long long k,x;
        scanf("%lld",&x);
        printf("Case #%ld: ",tst);
        if(x==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        //k=x;
        set<long long >st;

        for(int i=1;;i++)
        {
            k=x*i;
            while(k!=0)
            {
                st.insert(k%10);
                k/=10;
            }
            if(st.size()==10)
            {
                printf("%lld\n",x*i);
                break;
            }
        }
    }
}
