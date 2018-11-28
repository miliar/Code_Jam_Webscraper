#include <cstdio>
#include <cstring>

#define min(a, b) (a < b ? a : b)

using namespace std;

int M[128][128];
int n, m, T, C=1;
int vl[128], vc[128];

bool testa() {
    // inconst?
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++) {
            if (vl[i]!=-1 and M[i][j] < vl[i]) return false;
            if (vc[j]!=-1 and M[i][j] < vc[j]) return false;
            if (vl[i]!=-1 and vc[j]!=-1 and min(vl[i],vc[j]) != M[i][j]) return false;
            if (vl[i]!=-1 and vc[j]==-1 and M[i][j]!=vl[i]) {
                vc[j] = M[i][j];
                return testa();
            }
            if (vl[i]==-1 and vc[j]!=-1 and M[i][j]!=vc[j]) {
                vl[i] = M[i][j];
                return testa();
            }
        }


    return true;
}

bool testa0() {

    //axa coluna com a propriedade
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++)
        for (int k=i+1;k<n;k++)
            if (M[i][j] != M[k][j]) {
                int &a = vl[i];
                int &b = vc[j];
                int &c = vl[k];
                int t1 = M[i][j], t2 = M[k][j];
                if (t1 < t2) {
                    if (a != -1 and a != t1) return false;
                    a = t1;
                }
                else {
                    if (c != -1 and c != t2) return false;
                    c = t2;
                }
            }


    //axa linha com a propriedade
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++)
        for (int k=j+1;k<m;k++)
            if (M[i][j] != M[i][k]) {
                int &a = vc[j];
                int &b = vl[i];
                int &c = vc[k];
                int t1 = M[i][j], t2 = M[i][k];
                if (t1 < t2) {
                    if (a != -1 and a != t1) return false;
                    a = t1;
                }
                else {
                    if (c != -1 and c != t2) return false;
                    c = t2;
                }
            }
    return testa();
}

int main() {

    for (scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d %d",&n,&m);
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                scanf("%d",&M[i][j]);
        if (n==1 or m==1) {
            printf("YES\n");
            continue;
        }
        memset(vl,0xff,sizeof(vl));
        memset(vc,0xff,sizeof(vc));
        bool r=testa0();
        printf("%s\n",r?"YES":"NO");
/*        printf("  ");
        for (int i=0;i<m;i++) printf("%d ",vc[i]);
        printf("\n");
        for (int i=0;i<n;i++) {
            printf("%d ",vl[i]);
            for (int j=0;j<m;j++)
                printf("%d ",M[i][j]);
            printf("\n");
        }*/
    }

    return 0;
}
