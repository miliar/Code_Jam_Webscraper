#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <set>
using namespace std;

#define CLR(a,b) memset(a,b,sizeof(a))
const int N = 100 + 5;
int n,m;
char M[N][N];
int cnt[N][N][4];
int mp[1000];
void solve(){
    mp['^'] = 0;
    mp['>'] = 1;
    mp['v'] = 2;
    mp['<'] = 3;
    CLR(cnt, 0);
    int ans = 0;
    for(int i = 0 ; i < n ; i ++){
        int curr = 0;
        for(int j = 0 ; j < m ; j ++){
            cnt[i][j][3] = curr;
            if(M[i][j] != '.') curr ++;
        }
        curr = 0;
        for(int j = m-1 ; j >= 0 ;j --){
            cnt[i][j][1] = curr;
            if(M[i][j] != '.') curr ++;
        }
    }
    for(int i = 0 ; i < m ; i ++){
        int curr = 0;
        for(int j = 0 ; j < n ; j ++){
            cnt[j][i][0] = curr;
            if(M[j][i] != '.') curr ++;
        }
        curr = 0;
        for(int j = n-1 ; j >= 0 ;j --){
            cnt[j][i][2] = curr;
            if(M[j][i] != '.') curr ++;
        }
    }
    for(int i = 0 ; i < n ; i ++){
        for(int j = 0 ; j < m ; j ++){
            if(M[i][j] == '.')continue;
            int sum = 0;
            for(int k = 0 ; k < 4 ; k ++)sum += cnt[i][j][k];
            if(sum == 0){
                printf("IMPOSSIBLE\n");
                return;
            }
            if(M[i][j] != '.'){
                int dr = mp[M[i][j]];
                if(cnt[i][j][dr] == 0)ans ++;
            }
        }
    }
    printf("%d\n",ans);
}
int main()
{
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d",&T);
    while(T--){
        cas ++;
        printf("Case #%d: ",cas);
        scanf("%d%d",&n,&m);
        for(int i = 0 ; i < n ; i ++){
            scanf("%s",M[i]);
        }
        solve();
    }
    return 0;
}