#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
struct cell{
    int x,y,val;
    cell(int xx,int yy,int v):x(xx),y(yy),val(v){}
    bool operator < (const cell &o ) const{ return val<o.val;}
};

bool row[110],col[110];


void solve(){
    int n,m;
    scanf("%d %d",&n,&m);
    vector<cell> v;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            int q;
            scanf("%d",&q);
            v.push_back(cell(i,j,q));
        }
    }
    sort(v.rbegin(),v.rend());
    memset(row,0,sizeof(row));
    memset(col,0,sizeof(col));
    int nVal=101;
    int idx=0;
    while(idx<v.size()){
        int k=idx;
        while(k+1<=v.size()&&v[k].val==v[idx].val)k++;

        for(int p=idx;p<k;p++){
            if(row[v[p].x]&&col[v[p].y]){
                printf("NO\n");return;
            }
        }
        for(;idx<k;idx++){
            row[v[idx].x]=col[v[idx].y]=true;
        }
    }
    printf("YES\n");
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int t=1;t<=n;t++){
        printf("Case #%d: ",t);
        solve();
    }
}
