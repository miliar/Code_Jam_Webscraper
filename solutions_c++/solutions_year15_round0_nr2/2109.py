#include<iostream>
#include<cstdio>
#include<cstring>
#include<set>
using namespace std;
const int  N  = 1000+10;
multiset<int> ss;
multiset<int>::iterator it;
int a[N];
int dp[N];
int get(int x,int a)
{
    int ans = 0;
    if(a<=x) return 0;
    if(a%x==0) return a/x-1;
    else return a/x;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
        int t,cas=0;
        cin>>t;
        while(t--){
            int n;ss.clear();
            cin>>n;
            for(int i=1;i<=n;i++) { scanf("%d",&a[i]);ss.insert(a[i]);}
            it = ss.end(); it--; int ma = *it;
            int ans = 1000;
            for(int i=1000;i>=1;i--){
                int x = 0;
                for(int j=1;j<=n;j++){
                    x += get(i,a[j]);
                }
                ans = min(ans, x+i);
            }
            printf("Case #%d: %d\n",++cas,ans);
        }
        return 0;
}
