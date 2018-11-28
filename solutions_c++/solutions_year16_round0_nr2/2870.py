#include <bits/stdc++.h>
#define ll long long
using namespace std;

char ch[102];

int main()
{
    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);


    int a,b,c,d,e,x,y,z,t,n,m;

    scanf("%d",&t);

    for(int te=1;te<=t;te++)
    {
        printf("Case #%d: ",te);

        scanf("%s",ch);
        n=strlen(ch);

        x=0;

        for(a=n-1;a>=0;a--)
        {
            if(ch[a]=='+') continue;
            for(b=a;b>=0;b--)
            {
                if(ch[b]=='-') ch[b]='+';
                else ch[b]='-';
            }
            x++;
        }
        cout<<x<<endl;
    }

    return 0;
}
