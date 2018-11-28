#include<cstdio>
#include<cstdlib>

using namespace std;
#define REP(i,a,b)\
    for(int(i)=int(a);i<=int(b);i++)

int cards[2][4];
int possiblecount[16];
int main(){
    int T,N1,N2,count,casectr,temp;
    scanf("%d",&T);
    casectr = T;
    while(T--){
        count = 0;
        REP(i,0,15)
            possiblecount[i]=0;
        scanf("%d",&N1);
        REP(i,0,3)
            REP(j,0,3){
                if(i==(N1-1))
                    scanf("%d",&cards[0][j]);
                else
                    scanf("%d",&temp);
        }
        scanf("%d",&N2);
        REP(i,0,3)
            REP(j,0,3){
                if(i==(N2-1))
                    scanf("%d",&cards[1][j]);
                else
                    scanf("%d",&temp);
        }
        REP(i,0,1)
            REP(j,0,3)
                possiblecount[cards[i][j]-1]++;
        REP(i,0,15)
            if(possiblecount[i]>1){
                temp = i+1;
                count++;
            }
        switch(count){

            case 0: printf("Case #%d: Volunteer cheated!\n",casectr-T);
                    break;
            
            case 1: printf("Case #%d: %d\n",casectr-T,temp);
                    break;
            
            case 2: printf("Case #%d: Bad magician!\n",casectr-T);
                    break;

            case 3: printf("Case #%d: Bad magician!\n",casectr-T);
                    break;

            case 4: printf("Case #%d: Bad magician!\n",casectr-T);
                    break;
        }
    }
    return 0;
}
