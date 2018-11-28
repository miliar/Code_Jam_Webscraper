
#include <bits/stdc++.h>
#define FOR(i,a,b) for(int i = (a) ; i<b ; i++)
#define Set(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define pb push_back
#define all(v) (v.begin(), v.end())
typedef long long LL;
using namespace std;
LL MOD = 1e9+7;
int arr[1009];

int main()
{
    ios_base::sync_with_stdio(0);
    //freopen("input.in", "r", stdin);
    //freopen("output.txt", "w", stdout);

    int t;cin>>t;
    int kase=0;
    while(t--)
    {
        int n;
        cin>>n;
        int maxi=0;
        FOR(i,0,n)cin>>arr[i],maxi=max(maxi,arr[i]);
        int mini=1e9;
        FOR(i,1,maxi+1)
        {
            int c=0;
            FOR(j,0,n)
                if(arr[j]>i)
                 c+= ((arr[j]+i-1)/i)-1;
            mini = min(mini,c+i);
        }

        cout << "Case #" << ++kase << ": " << mini <<endl;
    }

    return 0;
}
