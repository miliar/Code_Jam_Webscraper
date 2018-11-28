#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define sd(x) scanf("%d",&x)
#define sfd(x) scanf("%d",&x)
#define pf printf

#define LL long long
#define ll long long
#define LD long double
#define ld long double
#define PB push_back
#define pb push_back
#define MP make_pair
#define mp make_pair
#define F first
#define S second

typedef pair<int,int> PII;
typedef vector<int> VI;

#define pii pair<int,int>
#define vi vector<int>
#define fr(i,n) for( int i=0; i<=n; i++)
#define frm(i,m,n) for(int i=m; i<=n; i++)

long double arr[1000],brr[1000];
void solve()
{
    int n;
    sd(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    for(int i=0;i<n;i++)
        cin>>brr[i];
    sort(arr,arr+n);
    sort(brr,brr+n);
    int ans1 = 0,ans2 = 0,p = n-1,q = n-1;
    for(int i=0;i<n;i++)
    {
        if(arr[p] > brr[q])
        {
            ans1++;
            q--;
            p--;
        }
        else
        {
            q--;
        }
    }
    int vis[2000]={0};
    for(int i = n-1;i>=0;i--)
    {
        int j = n-1;
        for(;j>=0;j--)
        {
            if(brr[j]>arr[i]&&vis[j]==0)
                break;
        }
        if(j == -1)
            ans2++;
        else
            vis[j] = 1;
    }
    cout<<ans1<<" "<<ans2<<endl;
}

int main()
{
    freopen("a.txt","r",stdin);
    freopen("sola.txt","w",stdout);
    int t,q=1;
    cin>>t;
    while(t--){
        printf("Case #%d: ",q++);
        // in();
    solve();
    }
}
