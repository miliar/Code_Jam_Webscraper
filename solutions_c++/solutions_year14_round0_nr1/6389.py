/**
   author:liuwen
*/
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
int a[5][5],used[20];
int main()
{
    //freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--){
        memset(used,0,sizeof(used));
        int f,s;
        scanf("%d",&f);
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                scanf("%d",&a[i][j]);
            }
        }
        for(int i=1;i<=4;i++)   used[a[f][i]]++;
        scanf("%d",&s);
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                scanf("%d",&a[i][j]);
            }
        }
        int ans=-1,t=0;
        for(int i=1;i<=4;i++){
            if(used[a[s][i]]==1){
                ans=a[s][i],t++;
            }
        }
        if(t==1)    printf("Case #%d: %d\n",++cas,ans);
        else if(t==0)   printf("Case #%d: Volunteer cheated!\n",++cas);
        else if(t>1)    printf("Case #%d: Bad magician!\n",++cas);
    }
    return 0;
}
