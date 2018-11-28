#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int m[5][5];
bool may[20];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;scanf("%d",&T);
    for(int cas = 1; cas <= T;cas++){
        memset(may,false,sizeof(may));
        int ans;
        scanf("%d",&ans);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++){
                scanf("%d",&m[i][j]);
                if(i == ans - 1) may[m[i][j]] = true;
            }
        scanf("%d",&ans);
        int num = 0,card;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++){
                scanf("%d",&m[i][j]);
                if(i == ans - 1){
                    if(may[m[i][j]]){
                        num++;
                        card = m[i][j];
                    }
                }
            }
        printf("Case #%d: ",cas);
        if(num == 1) printf("%d\n",card);
        else if(num > 1) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }

    return 0;
}
