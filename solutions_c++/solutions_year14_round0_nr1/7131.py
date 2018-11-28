#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
int main () {
    int row[4], ans, cards[4][4], T, y, cards1[4][4];
    scanf("%d",&T);
    for(int i=1; i<=T; i++){
        bool ansPresent=false, rep=false;
        scanf("%d",&ans);
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                scanf("%d",&cards[j][k]);
                if(ans-1==j) row[k]=cards[j][k];
            }
        }
        scanf("%d", &ans);
        ans--;
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                scanf("%d",&cards1[j][k]);
            }
        }
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                if(row[j]==cards1[ans][k]&&!rep){
                    if(ansPresent) rep=true;
                    ansPresent=true;
                    y=row[j];
                }
            }
        }
        if(rep) printf("Case #%d: Bad magician!\n",i);
        else if (ansPresent) printf("Case #%d: %d\n",i,y);
        else printf("Case #%d: Volunteer cheated!\n",i);
    }
};
