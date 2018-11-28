#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
typedef long long ll;
using namespace std;
int mp[110][110];
int r[110],c[110];
int main(){
    int t,T,i,j,n,m;
    freopen("B-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        scanf("%d %d",&n,&m);
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                scanf("%d",&mp[i][j]);
        for(i=1;i<=n;i++){
            r[i]=0;
            for(j=1;j<=m;j++)
                r[i]=max(r[i],mp[i][j]);
        }
        for(j=1;j<=m;j++){
            c[j]=0;
            for(i=1;i<=n;i++)
                c[j]=max(c[j],mp[i][j]);
        }
        bool flag=1;
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                if(!(mp[i][j]==c[j] || mp[i][j]==r[i])){
                    flag=0;
                    break;
                }
            }
            if(flag==0) break;
        }
        printf("Case #%d: ",t);
        if(flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
