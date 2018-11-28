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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps 1e-13
#define INF 0x3f3f3f3f
#define LL long long

using namespace std;
struct Node{
    int g,n;
};

Node f[10];
int T,d,ans,tot,a[10],fin[10];

void ask(int cnt){
    if(cnt==tot){
        int dt=0,lar=0;
        for(int i=0;i<tot;i++){
            dt+=(fin[i]-1)*f[i].n;
            lar=max(lar,f[i].g-f[i].g/fin[i]*(fin[i]-1));
        }
        ans=min(ans,lar+dt);
        return ;
    }
    fin[cnt]=1; ask(cnt+1);
    fin[cnt]=2; ask(cnt+1);
    fin[cnt]=3; ask(cnt+1);
}

int main(){
    ifstream cin("B-small-attempt7.in");
    ofstream cout("B-small-attempt7.out");
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        memset(a,0,sizeof(a));
        cin>>d;
        int t;
        while(d--){
            cin>>t;
            a[t]++;
        }
        tot=0;
        for(int i=1;i<10;i++) if(a[i]){
            f[tot].g=i;
            f[tot].n=a[i];
            tot++;
        }
        ans=INF;
        ask(0);
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    return 0;
}
/*

3
4
1 4 6 8
3
1 2 9


*/

