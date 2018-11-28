#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<ctime>
#include<bitset>
#define LL long long
#define db double
#define EPS 1e-8
#define inf 1e9

using namespace std;

int n,ans;
int mp[50][50],haha[50],father[50];
bool check(int x){
    if (x==n) return 1;
    int cntnum=0;
    for (int i=0;i<n;i++)
        if (!haha[i] && mp[father[x]][i]){
            ++cntnum;
            haha[i]=1;
            if (!check(x+1)) return 0;
            haha[i]=0;
        }
    return cntnum;
}
void solve(int x,int y,int z){
    if (z>=ans) return ;
    if (y==n) x++,y=0;
    if (x==n){
        memset(haha,0x00,sizeof(haha));
        bool ok=1;
        for (int i=0;i<n;i++) father[i]=i;
        do {
            if (!check(0)){
                ok=0;
                break;
            }
        }while (next_permutation(father,father+n));
        if (ok){
        ans=z;
        // caonimazheshenmegoubiwnayi
        // made kanbudong a
        //biebeichachong a
        }
        return ;
    }
    solve(x,y+1,z);
    if (!mp[x][y]){
        mp[x][y]=1;
        solve(x,y+1,z+1);
        mp[x][y]=0;
    }
}
int main(){
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int T,cas=1;
    scanf("%d",&T);
    while (T--){
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++){
                char ch;
                cin>>ch;
                if (ch=='1') mp[i][j]=1;
                else mp[i][j]=0;
            }
        ans=n*n;
        solve(0,0,0);
        printf("Case #%d: %d\n",cas++,ans);
        //haoxua xiwangbuyaobeichachongchachulaia
    }
    return 0;
}
