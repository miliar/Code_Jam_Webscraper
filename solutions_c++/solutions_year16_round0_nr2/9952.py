#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.o", "w", stdout);
    int t,f,n,i;
    scanf("%d",&t);
    for(int cs=1; cs<=t; cs++)
    {
        string a;
        cin>>a;
        int cnt=0;
        f=0;
        for(i=0; i<a.length(); i++)
        {
            if(a[i]=='-' && i==0)
            {
                f=1;
            }
            else if(a[i]=='+' && a[i+1]=='-')
            {
                cnt+= (1*2);
                i++;
            }
        }
        printf("Case #%d: %d\n",cs,cnt+f);
    }

    return 0;
}
