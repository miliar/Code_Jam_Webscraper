#include <cstdio>
#include <set>

using namespace std;

#define IMPRIMIR(X,Y,Z) printf("Case #%d: %d %d\n",(X),(Y),(Z))
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FOREACH(x,v) for (x =(v).begin(); x !=(v).end(); ++x)
#define REVEACH(x,v) for (x =(v).end()-1; x !=(v).begin(); --x)

typedef set<double>::iterator iterador;

int main () {

    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);


    int casos;
    scanf("%d",&casos);
    int k = 0;
    while (k < casos) {
        int bloques;
        scanf("%d",&bloques);
        set <double> Naomi,Naomi_Dc;
        set <double> Ken,Ken_Dc;

        double valor;
        FOR(i,0,bloques) {  scanf("%lf",&valor); Naomi.insert(valor);Naomi_Dc.insert(valor);}
        FOR(i,0,bloques) {  scanf("%lf",&valor); Ken.insert(valor); Ken_Dc.insert(valor);}

        iterador n_it,k_it;
        int War = bloques;
        FOREACH(n_it,Naomi)
            FOREACH(k_it,Ken)
                if (*n_it < *k_it) {
                    War--;
                    Ken.erase(k_it);
                    break;
                }


        int deceitful = 0;
        while (!Naomi_Dc.empty()) {
            if (*Naomi_Dc.begin() < *Ken_Dc.begin()) {
                Naomi_Dc.erase(Naomi_Dc.begin());
                Ken_Dc.erase(*Ken_Dc.rbegin());
            }else {
                Naomi_Dc.erase(Naomi_Dc.begin());
                Ken_Dc.erase(Ken_Dc.begin());
                deceitful++;
            }
        }

        /* SOLUCION UNICA CORRECTA
        double menor = -1*(*--Naomi_Dc.end());
        double mayor = -1*(*Ken_Dc.begin());

        Ken_Dc.erase(*Ken_Dc.begin());
        Naomi_Dc.erase(*--Naomi_Dc.end());

        if (menor > mayor) deceitful++;

        if (bloques > 1)
        FOREACH(n_it,Naomi_Dc)
                FOREACH(k_it,Ken_Dc)
                    if ((-1*(*n_it)) > (-1 * (*k_it))) {
                        deceitful++;
                        Ken_Dc.erase(k_it);
                        break;
                    }
        */


        IMPRIMIR(++k,deceitful,War);
    }

return 0;
}
