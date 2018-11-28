#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <set>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
#define MAXN 50010

int v[MAXN];
bool vis[MAXN];

int main(){
    int n;
    int nt;
    freopen ("A-large.in","r",stdin);
    freopen ("A.out","w",stdout);

    scanf(" %d",&nt);
    int t = 1;
    while(nt--){
        int x;
        scanf(" %d %d",&n,&x);
        for(int i = 0 ; i < n ; i++){
            scanf(" %d",&v[i]);
        }
        sort(v,v+n);
        memset(vis,0,sizeof(vis));
        int ans = 0;
        int i = 0;
        int j = n - 1;

        while(i <= j){
            if(i == j){
                ans++;
                break;
            }
            if(v[i] + v[j] > x){
                ans++;
                j--;
            }
            else{
                ans++;
                i++;
                j--;
            }
        }
        printf("Case #%d: %d\n",t++,ans);
    }
    return 0;
}
