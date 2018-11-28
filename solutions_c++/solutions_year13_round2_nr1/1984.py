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
int c;
int d[10000];
int ans;
void rek(int x,int y,int step){
    if (y>c){
        ans=min(ans,step);
    }
    else{
        if (x>d[y]){
            rek(x+d[y],y+1,step);
        }
        else{
            if (step<ans)rek(x,y+1,step+1);
            if (step<ans)rek(2*x-1,y,step+1);
        }
    }
}   
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&a);
    for (int i=1;i<=a;i++){
        ans=inf;
        scanf("%d %d",&b,&c);
        memset(d,0,sizeof(d));
        for (int j=0;j<c;j++){
            scanf("%d",&d[j]);
        }
        sort(d,d+c);
        if (b==1){
            ans=c;
        }
        else{
            rek(b,0,0);
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
