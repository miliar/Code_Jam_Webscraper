#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <cstdlib>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <deque>
#include <ctime>
#define s(n) scanf("%d",&n)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define vi vector<int>
#define ii pair<int,int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define LL long long
#define ULL unsigned long long
#define R freopen("in","r",stdin)
#define W freopen("out","w",stdout)
#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()
using namespace std;


int main()
{
    R;W;
    int t,c=0;cin>>t;
    while(t--)
    {
        c++;
        printf("Case #%d: ",c);
        int n;cin>>n;
        int cp;
        cin>>cp;
        int arr[10001];
        for(int i=0;i<n;i++)cin>>arr[i];
        sort(arr,arr+n);
        int ans=0;
        for(int i=0,j=n-1;i<=j;)
        {
            if(i==j){ans++;break;}
            else
            {
                if(arr[j]+arr[i]<=cp)
                {
                    ans++;
                    i++;j--;
                }
                else
                {
                    ans++;
                    j--;
                }
            }
        }
        cout<<ans<<endl;
    }
}
