//Template of CyberKasumi (Jennifer Santoso a.k.a. Liang Qiuxia)

#include <vector>
#include <list>
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
#include <queue>
using namespace std;

#define LL long long
#define inf 2123123123
#define MOD 1000000007


int a;
int b;
int n,m;
int t[1000][1000];
int hori[1000];
int verti[1000];
int mapping[1000][1000];
bool check(){
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (t[i][j]!=mapping[i][j])
            return false;
        }
    }
    return true;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&a);
    for (int z=1;z<=a;z++){
        memset(hori,0,sizeof(hori));
        memset(verti,0,sizeof(verti));
        memset(t,0,sizeof(t));
        memset(mapping,0,sizeof(mapping));
        scanf("%d %d",&n,&m);
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                scanf("%d",&t[i][j]);
            }
        }
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                hori[i]=max(hori[i],t[i][j]);
                verti[j]=max(verti[j],t[i][j]);
            }
        }
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                mapping[i][j]=min(hori[i],verti[j]);
            }
        }
        if (check())printf("Case #%d: YES\n",z);
        else printf("Case #%d: NO\n",z);
    }
    //while(1);
    return 0;
}
