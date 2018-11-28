#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cctype>
#define ll long long
#define ld long double
#define sqr(a) (a)*(a)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define inf (int)1e9
using namespace std;
const int N=1002;
ld a[N],b[N];
int t,n,ans1,ans2,ans;
bool used[N];
int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    freopen("D-large.in","r",stdin);
    freopen("3.out","w",stdout);
    cin>>t;
    for(int e=1;e<=t;e++)
    {
        ans2=ans1=ans=0;
        cin>>n;
        for(int i=0;i<n;i++) cin>>a[i],used[i]=0;
        for(int i=0;i<n;i++) cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
            if (b[j]>a[i] && !used[j]) {used[j]=1;ans2++;break;}
        ans2=n-ans2;
        reverse(b,b+n);
        for(int i=0;i<n;i++){
                int k=0;
            for(int j=i,pos=n-1;j<n;j++,pos--)
            if (a[pos]>b[j]) k++;
            if (k==n-i) {ans1=k;break;}
        }
        cout<<"Case #"<<e<<": "<<ans1<<' '<<ans2<<endl;

    }
    return 0;
}
