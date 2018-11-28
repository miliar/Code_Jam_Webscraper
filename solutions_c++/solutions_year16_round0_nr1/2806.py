#include <bits/stdc++.h>
#define ll long long
using namespace std;



int main()
{
    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);


    int a,b,c,d,e,x,y,z,t,n,m;

    scanf("%d",&t);

    for(int te=1;te<=t;te++)
    {
        printf("Case #%d: ",te);

        scanf("%d",&n);

        bool bi[11];

        for(a=0;a<=9;a++) bi[a]=false;

        if(!n)
        {
            printf("INSOMNIA\n");
            continue;
        }

        ll x;

        e=0;
        for(a=1;;a++)
        {
            x=1ll*a*n;
            while(x>0)
            {
                b=x%10;
                x=x/10;
                if(!bi[b]) e++;
                bi[b]=true;
            }
            if(e==10) break;
        }
        cout<<1ll*a*n<<endl;
    }

    return 0;
}
