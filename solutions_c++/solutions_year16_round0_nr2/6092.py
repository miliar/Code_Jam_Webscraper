#include <bits/stdc++.h>
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MOD 1000000007
#define lli long long int
#define li long int

using namespace std;

char s[110];
int f(int l)
{   int i,p=0,n=0;
    for(i=0;i<l;i++)
    {   if(s[i]=='+') p++;
        else n++;
    }
    if(n==0) return 0;
    if(p==0) return 1;
    while(s[l-1]=='+')
        l--;
    for(i=0;i<l;i++)
    {   if(s[i]=='+') s[i]='-';
        else s[i]='+';
    }
    return 1+f(l);
}
int main()
{   ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {   cin>>s;
        cout<<"Case #"<<i<<": ";
        cout<<f(strlen(s))<<endl;
    }
    return 0;
}
