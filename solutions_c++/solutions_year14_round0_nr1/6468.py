#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
using namespace std;
set<int>s;
int a[5][5];
int b[5][5];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,cas=0; scanf("%d",&T);
    while(T--){
        int x,y;
        s.clear();
        scanf("%d",&x);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++){
                if(a[x][i]==b[y][j]){
                    s.insert(a[x][i]);
                }
            }
        printf("Case #%d: ",++cas);
        if(s.size()==1){
            set<int>::iterator it=s.begin();
            printf("%d\n",*it);
        }
        else if(s.size()>1){
            printf("Bad magician!\n");
        }
        else{
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
