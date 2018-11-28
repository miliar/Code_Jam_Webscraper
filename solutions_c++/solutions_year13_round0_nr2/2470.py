#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

int a[110][110];
//bool can[110][110];

struct node{
    int x,y,v;
};
vector<node> v;

bool cmp(node a, node b) {
    return a.v<b.v;
}

int main() {
    //freopen("p.txt","r",stdin);
    //freopen("s.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++) {
        //memset(can,0,sizeof(can));
        v.clear();
        int n,m;
        int idx=0;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                scanf("%d",&a[i][j]);
                node one;
                one.x=i;
                one.y=j;
                one.v=a[i][j];
                v.push_back(one);
            }
        }
        sort(v.begin(),v.end(),cmp);
        int i,j,sz=v.size();
        for(i=0;i<sz;i++) {
            int val=v[i].v;
            int x=v[i].x;
            int y=v[i].y;
            bool flag1=true,flag2=true;
            for(j=0;j<n;j++) {
                if(a[j][y]>val){
                    flag1=false;
                    break;
                }
            }
            for(j=0;j<m;j++) {
                if(a[x][j]>val) {
                    flag2=false;
                    break;
                }
            }
            if(flag1==false&&flag2==false) {
                break;
            }
        }
        if(i>=sz) printf("Case #%d: YES\n",cs);
        else printf("Case #%d: NO\n",cs);

    }
    return 0;
}
