#include<bits/stdc++.h>
typedef long long int lli;
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    int tt;
    cin>>tt;
    for(int k=1; k<=tt; k++)
    {
        char s[1010],a[1010],b[1010];

        cin>>s;
        lli len=strlen(s);

        a[0]=s[0];
        lli  i;
        for(i=1; i<len; i++)
        {
            if(s[i]<a[0])
            {
                a[i]=s[i];
            }
            else
            {
                break;
            }
        }
        lli n=i;
        lli m=0;
        if(i<len)
        {
            b[0]=s[i];
            i++;
            m=1;
            for(; i<len; i++)
            {
                if(s[i]<b[m-1])
                {
                    a[n]=s[i];
                    n++;
                }
                else
                {
                    b[m]=s[i];
                    m++;
                }
            }
        }
        cout<<"Case #"<<k<<": ";
        for(int i=m-1; i>=0; i--)
        {

            cout<<b[i];
        }
        for(int i=0; i<n; i++)
        {

            cout<<a[i];
        }
        cout<<endl;


    }

    return 0;
}
