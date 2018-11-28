#include<bits/stdc++.h>
#define mp make_pair
#define PII pair<int,int>
#define fi first
#define se second
using namespace std;

const int NMAX=105;

int t,n,a[NMAX];
char s[NMAX];

int main()
{
    int i,k,len;
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    cin.sync_with_stdio(false);
    cin>>t;
    for (k=1;k<=t;k++)
    {
        cin>>(s+1);
        n=1;a[1]=0;
        if (s[1]=='+') a[1]=1;
        len=strlen(s+1);
        for (i=2;i<=len;i++)
            if (s[i]!=s[i-1])
            {
                n++;a[n]=0;
                if (s[i]=='+') a[n]=1;
            }
        if (a[n]==1) n--;
        cout<<"Case #"<<k<<": "<<n<<"\n";
    }
    return 0;
}

