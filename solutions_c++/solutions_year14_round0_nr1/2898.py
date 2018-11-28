#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
int cnt[20];
int main()
{
    int T,i,j,tt,row,cas=1;
    scanf("%d",&T);
    while(T--){
        vector<int> v;
        memset(cnt,0,sizeof(cnt));
        scanf("%d",&row);
        for (i=1;i<=4;i++){
            for (j=1;j<=4;j++){
                scanf("%d",&tt);
                if (row==i) cnt[tt]++;
            }
        }
        scanf("%d",&row);
        for (i=1;i<=4;i++){
            for (j=1;j<=4;j++){
                scanf("%d",&tt);
                if (row==i&&cnt[tt]) v.push_back(tt);
            }
        }
        printf("Case #%d: ",cas++);
        if (v.size()==0) puts("Volunteer cheated!");
        else if (v.size()>1) puts("Bad magician!");
        else printf("%d\n",v[0]);
    }
    return 0;
}
