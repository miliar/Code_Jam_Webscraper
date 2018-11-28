#include<bits/stdc++.h>
#define MOD 1000000007
#define MX 100010
#define ll long long
#define sc(n) scanf("%d",&n)
#define pr(m) printf("%d\n",m)
#define pi acos(-1.0)

using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("OutAlarge.txt","w",stdout);
    int t,tc=1,i;
    string a;

    sc(t);
    while(t--)
    {
        cin>>a;
        int l=a.size();
        string b;
        b="";
        b+=a[0];
        for(i=1;i<a.size();i++){
            if(a[i]<b[0])b+=a[i];
            else b=a[i]+b;
        }
        cout<<"Case #"<<tc++<<": "<<b<<endl;

    }

    return 0;
}
