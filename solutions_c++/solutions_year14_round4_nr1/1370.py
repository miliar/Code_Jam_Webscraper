#include<bits/stdc++.h>

using namespace std;

#define vi vector < int >
#define pb push_back
#define mp make_pair
#define ll long long
#define llu unsigned long long
#define MOD 1000000007
#define INF 2000000000
#define dbg(x) { cout<< #x << ": " << (x) << endl; }
#define all(x) x.begin(),x.end()

int a[10004];
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int tc=1,t,n,x,i;
    scanf("%d",&t);
    while(t--){
        cin>>n>>x;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }
        sort(a,a+n);
        int ans = n;
        int i = 0 ,j= n-1;
        while(i<j){
            while(j>i && (a[i] + a[j] > x))
                j--;
            if(j>i && a[i] + a[j] <= x){
                ans--;
                i++;
                j--;
            }
            else{
                break;
            }
        }
        printf("Case #%d: %d\n",tc++,ans);
    }
    //system("pause");
    return 0;
}
