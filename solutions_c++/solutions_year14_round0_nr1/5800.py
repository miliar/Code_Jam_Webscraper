#include <cstdio>
using namespace std;

int main(int argc, char const *argv[]) {
    int T,row,dummy,cards[4],card,cnt,picked;

    scanf("%d",&T);
    for(int ca=1; ca<=T; ++ca) {
        scanf("%d",&row);
        for(int i=0; i<4; ++i) {
            for(int j=0; j<4; ++j)
                if (row == i+1)
                    scanf("%d",&cards[j]);
                else
                    scanf("%d",&dummy);
        }

        picked = 0;
        cnt = 0;
        scanf("%d",&row);
        for(int i=0; i<4; ++i) {
            for(int j=0; j<4; ++j) {
                scanf("%d",&card);
                if (row == i+1)
                    for(int k=0; k<4; ++k)
                        if (card == cards[k]) {
                            picked = card;
                            ++cnt;
                            break;
                        }
            }
        }

        if (0 == cnt)
            printf("Case #%d: Volunteer cheated!\n",ca);
        else if (1 == cnt)
            printf("Case #%d: %d\n",ca,picked);
        else
            printf("Case #%d: Bad magician!\n",ca);
            
    }
    return 0;
}
