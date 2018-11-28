#include <iostream>
#include <string.h>
using namespace std;
#define ll long long
int main()
{   ll n,j;
    cin>>n;
    for(j=0;j<n;++j)
    {   string s;
    cin>>s;
    ll i,e,b,l=0;
    while(s[l]!='\0')
        ++l;
    char c[2*l];
    c[l-1]=s[0];
    b=l-1;
    e=l-1;
    for(i=1;i<l;++i)
    {   if(s[i]>=c[b])
        {   c[b-1]=s[i];
            b--;
        }
        else
        {   c[e+1]=s[i];
            e++;
        }
    }
    cout<<"Case #"<<j+1<<": ";
    for(i=b;i<=e;i++)
        cout<<c[i];
    cout<<"\n";
    }
    return 0;
}
