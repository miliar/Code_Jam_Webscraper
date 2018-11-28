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
#include <stack>
#include <set>
#include <map>
#include <string>
#include <deque>
#include <ctime>
#define s(n) scanf("%d",&n)
#define ss(n) scanf("%s",n)
#define s2(a,b) scanf("%d%d",&a,&b)
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
using namespace std;
int arr[1111];
int res[1111];
int main()
{
    R;W;
    int t;cin>>t;
    int c =0;
    
    while(t--)
    {
        c++;
        cout<<"Case #"<<c<<": ";
        int n;cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        int ans = 1000;
        
        for(int i=1;i<=ans;i++)
        {
            int sum =0;
            for(int j=0;j<n;j++)
            {
                if(i<arr[j])
                {
                    int x = arr[j]/i;
                    while((i*x)<arr[j])
                        x++;
                    sum += (x-1);
                }
                
            }
            
            ans = min(ans,i+sum);
        }
        cout<<ans<<endl;
    }
}