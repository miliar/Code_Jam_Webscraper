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

#define PI 3.141592653589793
int main()
{
    //read();
    //freopen("out.txt","w",stdout);
    int test, kase=1;
    cin>>test;
    while(test--)
    {
        int diner;
        cin>>diner;
        int arr[diner+1];
        int maxDish=0;
        for( int i =0; i<diner ; i++) {
                cin>>arr[i];
                maxDish = max(maxDish, arr[i]);
        }
        sort(arr,arr+diner);
        int ans = INT_MAX;
        for( int dish = 1 ; dish <=maxDish; dish++)
        {
            int total =0;
            for( int i =0; i<diner; i++)
            {
                if(arr[i]>=dish)
                {
                    total+=(ceil((double)arr[i]/dish)-1);
                }
            }
            total+=dish;

            ans = min(ans, total);
        //cout<<ans<<ends<<dish<<endl;
        }
        printf("Case #%d: %d\n",kase++,ans);
    }
}
