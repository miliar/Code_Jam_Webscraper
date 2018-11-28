#include<bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define lol long long
#define ld long double
#define fc cin.tie(NULL);ios_base::sync_with_stdio(false);
using namespace std;
const int N=100005;
const int md=1000000007;

int t,c,n,i,j,x,q;
char u[11];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    fc
    cin>>t;
    while (t--)
    {
        ++c;
        cin>>n;
        for (i=0;i<10;++i)
         u[i]=0;
        q=0;
        i=1;
        while (!q && n!=0)
        {
            x=n*i;
            while (x>0)
            {
                ++u[x%10];
                x/=10;
            }
            q=1;
            for (j=0;j<10;++j)
             if (!u[j]) q=0;
            if (q) {x=n*i;break;}
            ++i;
        }
        cout<<"Case #"<<c<<": ";
        if (q) cout<<x;
        else cout<<"INSOMNIA";
        cout<<"\n";
    }
}
