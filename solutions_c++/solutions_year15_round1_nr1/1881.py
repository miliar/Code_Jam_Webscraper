#include <bits/stdc++.h>
#define mp make_pair
#define pii pair<int,int>
#define pb push_back
#define Max(a,b)a>b?a:b
#define Min(a,b)a<b?a:b
#define read() freopen("in.txt","r",stdin)
using namespace std;
template <typename T>
string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}
int Set( int n , int pos)
{
    return ( n=n | 1<<pos );
}
int reset(int N,int pos)
{
    return N= N & ~(1<<pos);
}
bool check(int N,int pos)
{
    return (bool)(N & (1<<pos));
}
typedef long long ll;

//bool comp(const node &lhs, const node &rhs) { return lhs.b < rhs.b; }
ll arr[10010];
#define PI 3.141592653589793
int main()
{
//    read();
//    freopen("out.txt","w",stdout);
    int test, kase=1;
    cin>>test;
    while(test--)
    {
        int no;
        cin>>no;
        ll maxi=-12121;

        for( int i =0; i<no ; i++) {
                cin>>arr[i];
                if(i!=0)
                maxi = max(maxi,arr[i-1]-arr[i]);
        }

        ll ans1 =0, ans2=0;
        for( int i =1; i<no; i++)
        {
            if(arr[i-1]-arr[i]>=0)
            ans1+=(arr[i-1]-arr[i]);

        }

        for( int i =0; i<no-1; i++)
        {
            if(arr[i]<=maxi)
            {
                ans2+=arr[i];
            }
            else
                ans2+=maxi;
        }
        printf("Case #%d: %lld %lld\n",kase++,ans1,ans2);
    }
}
