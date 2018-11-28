#include<iostream>
#include<cstdio>
#include<climits>
#include<cstring>
#include<string>
#include<vector>
#include<queue>
#include<set>

#define INF 100000
#define pb push_back
#define mo 1000000007
#define ll long long int
#define ld long double
#define mp make_pair
#define ull unsigned long long int

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T,i,j;
    ll k,c,s;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>k>>c>>s;
        if(k==1)
        {
            cout<<"1\n";
            continue;
        }
        if(c==1)
        {
            if(s>=k)
            {
                for(j=1;j<=k;j++)
                {
                    cout<<j<<" ";
                }
                cout<<"\n";
            }
            else
            {
                cout<<"IMPOSSIBLE\n";
            }
            continue;
        }
        if(s>=k-1)
        {
            for(j=2;j<=k;j++)
            {
                cout<<j<<" ";
            }
            cout<<"\n";
        }
        else
        {
            cout<<"IMPOSSIBLE\n";
        }
    }
    return 0;
}
