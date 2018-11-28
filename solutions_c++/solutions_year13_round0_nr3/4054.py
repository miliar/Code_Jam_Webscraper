#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>

#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<map>
#include<sstream>
#include<utility>



#define FOR(i, s, e) for(int i=s; i<e; i++)
#define loop(i, n) for(int i=0; i<n; i++)
#define getint(n) scanf("%d", &n)
#define pb(a) push_back(a)
#define ll long long
#define dd double
#define SZ(a) int(a.size())
#define read() freopen("input.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)
#define mem(a, v) memset(a, v, sizeof(a))
#define all(v) v.begin(), v.end()
#define pi acos(-1.0)
#define INF 1<<29
#define mod abs
#define pf printf
#define sf scanf
#define mp make_pair
#define paii pair<int, int>
#define padd pair<dd, dd>
#define pall pair<ll, ll>
#define fr first
#define sc second

using namespace std;

#define MAXX 38

ll ara[] = {
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004
};

int ifPalin(ll n)
{
    vector<int>res;
    while(n)
    {
        res.pb(n%10);
        n = n / 10;
    }


    for(int i=0, j=SZ(res)-1; i<=j; i++, j--)
    {
        if(res[i] != res[j])
        {
            return 0;
        }
    }
    return 1;
}



int main()
{

    //read();
    //write();
    int kases, kaseno = 0;
    cin>>kases;
    ll start, end;
    int cnt;
    ll s;

    int low, high, mid;

    while(kases--)
    {
        cnt = 0;
        cin>>start>>end;

        low = 0; high = MAXX;

        while(low<=high)
        {
            mid = (low+high)/2;

            if(ara[mid] < start)
            {
                low = mid+1;
            }
            else
            {
                high = mid-1;
            }
        }

        start = low;

        low = 0; high = MAXX;

        end++;

        while(low <= high)
        {
            mid = (low+high)/2;

            if(ara[mid] < end)
            {
                low = mid+1;
            }
            else
            {
                high = mid-1;
            }
        }

        end = low;


        cnt = end - start;


        /*
        s = sqrt(start-1);
        s++;

        while(s*s <=end)
        {
            camehere ++;
            if(ifPalin(s) && ifPalin(s*s))
            {
                cout<<s*s<<", "<<endl;
                cnt++;
            }
            s++;
        }

        //cout<<"looped "<<camehere<<" times"<<endl;
        */
        pf("Case #%d: ", ++kaseno);
        cout<<cnt<<endl;
    }

    return 0;
}

