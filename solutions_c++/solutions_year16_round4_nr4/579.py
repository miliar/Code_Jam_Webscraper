#include<bits/stdc++.h>
#include<unistd.h>
using namespace std ;
#define ll long long
#define N 200100
#define R 0
#define P 1
#define S 2
#define inf 0x3f3f3f3f

char mp[5][5];
bool v[5];
int n,ans,tmp;

bool gaop(int d, int x){
    if (d==x) return gaop(d+1,x);
    if (d==n){
        for (int i=0;i<n;i++) if (mp[x][i]=='1' && !v[i]) return true;
        return false;
    }
    int ok=0;
    for (int i=0;i<n;i++) if (mp[d][i]=='1' && !v[i]){
        v[i]=1;
        ok=1;
        if (!gaop(d+1,x)) return false;
        v[i]=0;
    }
    return ok;
}
bool check(){
    for (int i=0;i<n;i++){
        memset(v,0,sizeof v);
        if (!gaop(0,i)) return false;
    }
    return true;
}
void col(int s){
    if (s==n*n) {
        if (check()) {
    //        for (int i=0;i<n;i++) puts(mp[i]);
    //        cout<<tmp<<endl;
            ans=min(ans,tmp);
        }
        return;
    }
    int x=s/n,y=s%n;
    if (mp[x][y]=='0') {
        col(s+1);
        mp[x][y]='1';
        tmp++;
        col(s+1);
        mp[x][y]='0';
        tmp--;
    }else
    col(s+1);
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,cas=0;
    cin>>T;
    while (T--){
        ans=inf;tmp=0;
        cin>>n;
        int mx=(1<<n);
        for (int i=0;i<n;i++)scanf("%s",mp[i]);
        col(0);
        printf("Case #%d: %d\n",++cas,ans);
    }
}
