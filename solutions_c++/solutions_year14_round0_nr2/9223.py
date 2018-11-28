#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int t;
    double min,tiempoUsado,c,f,fi,x,res;
    cin >> t;
    for (int n = 1; n<=t;n++){
        cin >> c >> f >> x;
        tiempoUsado = 0.0;
        fi = 2.0;
        min = x/fi;
        while (tiempoUsado < min){
            res = tiempoUsado + x/fi;
            tiempoUsado += c/fi;
            fi +=f;
            if (min > res)
                min = res;
        }
        cout<<fixed << setprecision(7)<< "Case #"<<n << ": " << min << endl;
    }
    return 0;
}