#include <cstdio>

using namespace std;

int T, mat[5][5], moguci[17][102], results[102], r;

int main () {
    scanf("%d", &T);
    for(int i=1; i<=T; ++i) {
        scanf("%d", &r);
        r--;

        for(int j=0; j<4; ++j)
            for(int jj=0; jj<4; ++jj)
                scanf("%d", &mat[j][jj]);

        for(int j=0; j<4; ++j) moguci[mat[r][j]][i]++;

        scanf("%d", &r);
        r--;

        for(int j=0; j<4; ++j)
            for(int jj=0; jj<4; ++jj)
                scanf("%d", &mat[j][jj]);

        int b=-1, ans=0;
        for(int j=0; j<4; ++j) {
            if(moguci[mat[r][j]][i]) {
                if(b>0) results[i] = -2;
                else {
                    b=1;
                    ans = mat[r][j];
                }
            }
        }
        if(ans==0) results[i]=-1;
        else if(results[i]==0) results[i] = ans;
    }
    for(int i=1; i<=T; ++i) {
        printf("Case #%d: ", i);
        if(results[i]==-1) printf("Volunteer cheated!\n");
        else if(results[i]==-2) printf("Bad magician!\n");
        else printf("%d\n", results[i]);
    }
    return 0;
}
