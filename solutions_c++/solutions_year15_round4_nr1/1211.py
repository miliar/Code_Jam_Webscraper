#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <tr1/unordered_set>
#include <tr1/unordered_map>

using namespace std;
using namespace tr1;

const int maxn=105;

const int fx[]={-1,1,0,0};
const int fy[]={0,0,-1,1};

int n,m;
char s[maxn][maxn];

bool check(int x,int y){
    if(x<0 || y<0 || x>=n || y>=m)return false;
    return true;
}

void solve(){
    static int i,j,k,p,ans,flag;
    ans=0;
    for(i=0;i<n;i++)
    for(j=0;j<m;j++){
        if(s[i][j]=='.')continue;
        flag=0;
        for(p=0;p<4;p++)
        for(k=1;check(i+fx[p]*k,j+fy[p]*k);k++)
            if(s[i+fx[p]*k][j+fy[p]*k]!='.')flag|=1<<p;
        if(flag==0){
            puts("IMPOSSIBLE");
            return;
        }
        if(s[i][j]=='^' && (flag&1))continue;
        if(s[i][j]=='v' && (flag&2))continue;
        if(s[i][j]=='<' && (flag&4))continue;
        if(s[i][j]=='>' && (flag&8))continue;
        ans++;
    }
    printf("%d\n",ans);
}

int main(){
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    static int T,Cas;
    scanf("%d",&T);
    for(Cas=1;Cas<=T;Cas++){
        scanf("%d%d",&n,&m);
        static int i;
        for(i=0;i<n;i++)
            scanf("%s",s[i]);
        printf("Case #%d: ",Cas);
        solve();
    }
    return 0;
}
