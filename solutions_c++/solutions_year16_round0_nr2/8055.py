#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main ()
{
    freopen("B-large.in", "r", stdin);
	freopen("B-large.out","w",stdout);
    ll cases,caseno=0,num,i;
    scanf("%lld",&cases);

    while(cases--)
    {
        string x;
        cin>>x;
        printf("Case #%lld: ",++caseno);
        ll l=x.size();
        for (i=0;i<l;i++)
        {
            if (x[i]=='-')
                break;
        }
        if (i==l)
        {
            printf("0\n");
            continue;
        }
        char ch=x[0];
        ll c=0;
        for (i=1;i<l;i++)
        {
            if (x[i]!=ch)
            {
                c++;
                ch=x[i];
            }
        }
        if (x[l-1]=='-')
            c++;
        printf("%lld\n",c);
    }
    return 0;
}
