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

void in()
{

}

void solve()
{
    int arr[5][5],brr[5][5];
    int a,b;
    cin>>a;
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            cin>>arr[i][j];
    cin>>b;
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            cin>>brr[i][j];
    int cnt[17] = {0};
    for(int i=1;i<=4;i++)
    {
        cnt[arr[a][i]]++;
        cnt[brr[b][i]]++;
    }
    int ans = 0,p;
    for(int i=1;i<=16;i++)
    {
        if(cnt[i]==2)
        {
            ans++;
            p =i;
        }
    }
    if(ans==1){
        cout<<p<<endl;
    }
    else if (ans==0)
    {
        cout<<"Volunteer cheated!"<<endl;

    }
    else
    {
        cout<<"Bad magician!"<<endl;
    }
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
