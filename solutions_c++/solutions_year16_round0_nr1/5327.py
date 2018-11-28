#include <bits/stdc++.h>
#define fr freopen("input.in","r",stdin)
#define fw freopen("output.out","w",stdout)
#define iOs ios_base::sync_with_stdio(false);
#define INF 111313131
#define all(x) (x).begin(), (x).end()
#define debug cout<<"here\n"
#define debugin cout<<"inhere\n"
#define debugname cout<<"dharmang\n";
using namespace std;
#define pb push_back
#define mp make_pair
#define sc second
#define fir first
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
int main()
{
    #ifndef ONLINE_JUDGE
        fr;fw;
    #endif
    iOs;
    int t; cin>>t;
    for(int i=1;i<=t;i++)
    {
        int counter=0,n,m,r,q,ans=0,j=2; cin>>n; q=n;
        int a[10]; memset(a,0,sizeof(a));
        x:
        m=q;
        if(n==0) {cout<<"Case #"<<i<<": "<<"INSOMNIA\n"; continue;}
        while(m>0)
        {
            r=m%10;
            m/=10;
            if(a[r]==0) counter++;
            a[r]++;
        }
        if(counter!=10)
        {
            q=n;
            q*=j;
            j++;
            goto x;
        }
        cout<<"Case #"<<i<<": "<<q<<endl;
    }
    return 0;
}
