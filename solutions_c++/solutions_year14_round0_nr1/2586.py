#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include <algorithm>
#define maxn 10010
#define maxx_N 26
#define INF 0x7fffffff
#define eps 1e-6

using namespace std;
int card[4][4];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int cas,test=1;
    scanf("%d",&cas);
    while(cas--){
        int row1,row2,k;
        int hash[20]={0},cheated=1,bad=0;
        scanf("%d",&row1);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&card[i][j]);
            }
        }
        for(int i=0;i<4;i++)hash[card[row1-1][i]]=1;
        scanf("%d",&row2);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&card[i][j]);
            }
        }
        for(int i=0;i<4;i++){
            if(hash[card[row2-1][i]]){
                k = card[row2-1][i];
                cheated = 0;
                bad++;
            }
        }
        printf("Case #%d: ",test++);
        if(cheated)
            printf("Volunteer cheated!\n");
        else if(bad>1)
            printf("Bad magician!\n");
        else
            printf("%d\n",k);
    }
    return 0;
}
