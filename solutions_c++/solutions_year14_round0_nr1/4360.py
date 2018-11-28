#include <cstdio>

#define SIZE 4
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define IMPRIMIR(X,Y) printf("Case #%d: %d\n",(X+1),(Y))
#define CHEATED(X) printf("Case #%d: Volunteer cheated!\n",(X+1))
#define BAD(X) printf("Case #%d: Bad magician!\n",(X+1))

int main () {

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    int casos;
    scanf("%d",&casos);
    int k = 0;
    while (k < casos) {
        int resp1,resp2;
        int basura;
        int sol1[SIZE];
        int sol2[SIZE];
        scanf("%d",&resp1);
        FOR(i,0,SIZE) {
            FOR (j,0,SIZE) {
                if (i == resp1-1) scanf("%d",&sol1[j]);
                else              scanf("%d",&basura);
            }
        }

        scanf("%d",&resp2);
        FOR(i,0,SIZE) {
            FOR(j,0,SIZE) {
                if (i == resp2-1) scanf("%d",&sol2[j]);
                else              scanf("%d",&basura);
            }
        }
        int iguales = 0;
        int valor;

        FOR(i,0,SIZE) {
            FOR(j,0,SIZE) {
                if (sol1[i] == sol2[j]) {
                    iguales++;
                    valor = sol1[i];
                }
            }
        }

        if (iguales == 1)
            IMPRIMIR(k,valor);
        else {
            iguales == 0 ? CHEATED(k) : BAD(k);
        }

        k++;
    }

return 0;
}
