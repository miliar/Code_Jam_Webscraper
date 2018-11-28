/*
| Problem Status : UNSOLVED
|
|
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<iterator>
#include<vector>
#include<string>
#include<sstream>
#include<set>
#include<deque>
#include<cstring>
#include<cstdlib>


#define FOR(i,v,n) for(int i=v;i<n;++i)
#define PVector(arr,type) copy(arr.begin(),arr.end(),ostream_iterator<type>(cout," "));
#define swap(a,b) { a=a^b; b=a^b; a=a^b; }

using namespace std;
typedef long long ll;


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;cin>>t;
    vector<vector<int> > arr(105,vector<int>(105));
    bool bad;
    for(int i=1;i<=t;++i)
    {
        int n,m;
        cin>>n>>m;

        FOR(a,0,n) FOR(b,0,m) cin>>arr[a][b];
        FOR(a,0,n) FOR(b,0,m)
        {
            bad=false;
            if(arr[a][b])
            {
                FOR(p,0,m) if(arr[a][p]>arr[a][b]) { bad=true; break; }
                if(bad)
                FOR(p,0,n) if(arr[p][b]>arr[a][b]) { cout<<"Case #"<<i<<": NO\n"; goto my; }
            }
        }
        cout<<"Case #"<<i<<": YES\n";
        my:;
        //cout<<"\n"<<n<<" "<<m;;
    }


    return 0;
}
