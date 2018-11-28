#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
int t,n;
int i,k,j,h;
double aux;
int y,z;
int prim;

    cin >> t;
    i = 1;
    for (i = 1; i <= t; i++){

        cin >> n;
        vector <double> nao, nao2, ken, ken2;

        for (k = 1; k <= n; k++){
            scanf("%Lf", &aux);
            nao.push_back(aux);
            nao2.push_back(aux);
        }
        for (k = 1; k <= n; k++){
            scanf("%Lf", &aux);
            ken.push_back(aux);
            ken2.push_back(aux);
        }

        sort (nao.begin(), nao.end(), greater<double>());
        sort (nao2.begin(), nao2.end(), greater<double>());
        sort (ken.begin(), ken.end(), greater<double>());
        sort (ken2.begin(), ken2.end(), greater<double>());


       y = 0;
        while (nao.size()){
            j = 1;
            while (j){
                if (nao[j-1] < ken[0]){
                    prim = j-2; //el anterior es el mas chico de nao necesario para ganar
                    if (prim >= 0){
                        nao.erase(nao.begin()+j-2, nao.begin()+j-1);
                        y++;
                    }
                    else nao.erase(nao.begin()+nao.size()-1, nao.begin()+nao.size());
                    ken.erase(ken.begin()+0, ken.begin()+1);

                    break;
                }
                if (j == nao.size()){
                    //si no hay una madera de nao que sea menor a la de nao
                    // se va a usar la madera mas liviana de nao
                    nao.erase(nao.begin()+nao.size()-1, nao.begin()+nao.size());
                    ken.erase(ken.begin()+0, ken.begin()+1);
                    y++;
                    break;
                }
                j++;
            }

        }






        z = 0;
        while (ken2.size()){
            j = 1;
            while (j){
                if (ken2[j-1] < nao2 [0]){ //j-1 es el actual
                    prim = j-2; //el anterior es el mas chico de ken necesario para ganar
                    if (prim >= 0) ken2.erase(ken2.begin()+j-2, ken2.begin()+j-1);
                    else ken2.erase(ken2.begin()+ken2.size()-1, ken2.begin()+ken2.size());
                    nao2.erase(nao2.begin()+0, nao2.begin()+1);
                    if (prim == -1) z++;// no hay anterior de ken so nao wins
                    break;
                }
                if (j == ken2.size()){
                    //si no hay una madera de ken que sea menor a la de nao
                    // se va a usar la madera mas liviana de ken
                    ken2.erase(ken2.begin()+ken2.size()-1, ken2.begin()+ken2.size());
                    nao2.erase(nao2.begin()+0, nao2.begin()+1);
                    break;
                }
                j++;
            }

        }










        cout << "Case #" << i << ": " << y << " " << z << endl;
    }


    return 0;
}
