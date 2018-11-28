#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int test, Case = 0;
    scanf("%d",&test);

    while (test--) {
        int q1, q2;
        int before[4][4];
        int after[4][4];

        scanf("%d",&q1);

        for (int i=0 ; i<4 ; i++) {
            for (int j=0 ; j<4 ; j++) {
                scanf("%d",&before[i][j]);
            }
        }

        scanf("%d",&q2);

        for (int i=0 ; i<4 ; i++) {
            for (int j=0 ; j<4 ; j++) {
                scanf("%d",&after[i][j]);
            }
        }

        int cnt = 0, ans = 0;

        for (int i=0 ; i<4 ; i++) {
            for(int j=0 ; j<4 ; j++)
                if(before[q1-1][i]==after[q2-1][j]) {
                    cnt++;
                    ans = before[q1-1][i];
                }
        }

        if(!cnt) printf("Case #%d: Volunteer cheated!\n",++Case);
        else if(cnt>1) printf("Case #%d: Bad magician!\n",++Case);
        else if(cnt==1) printf("Case #%d: %d\n",++Case, ans);


    }
    return 0;
}
