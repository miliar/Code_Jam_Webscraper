#include <cstdio>
#include <cstring>

using namespace std;

int T, C=1, r1, r2;
bool pode[32];

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d",&r1); r1--;
        memset(pode,true,sizeof(pode));
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++) {
                int t;
                scanf("%d",&t);
                if (i != r1)
                    pode[t]=false;
            }
        scanf("%d",&r2); r2--;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++) {
                int t;
                scanf("%d",&t);
                if (i != r2)
                    pode[t]=false;
            }
        int resp=-1;
        for (int i=1;i<=16;i++)
            if (pode[i]) {
                if (resp==-1)
                    resp = i;
                else
                    resp = -2;
            }
        if (resp==-1)
            printf("Volunteer cheated!\n");
        else if (resp==-2)
            printf("Bad magician!\n");
        else
            printf("%d\n",resp);
    }

    return 0;
}
