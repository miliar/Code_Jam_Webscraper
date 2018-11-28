#include <iostream>
#include <iomanip>
using namespace std;

long double C; //coste de comprar una granja
long double F; //extra cookies per second
long double X; //objetivo



long double solve(){
  long double tiempoTotal=0;
  long double ratio=2.0; //numero actual de cookies per second
  long double timeAct;
  long double timePredict;
  long double aux;
  while(true){
    //si no compramos mas
    timeAct=X/ratio;

    //si compramos una granja
    timePredict=C/ratio; //conseguimos galletas suficientes
    aux=timePredict; //guardamos este valor
    ratio+=F; //aumenta el ratio
    timePredict += X/ratio;

    if(timeAct <= timePredict){
      tiempoTotal+=timeAct;
      return tiempoTotal;
    } else {
      tiempoTotal+=aux;
    }
  }

}
int main(){
  int nCasos;
  cin >> nCasos;
  int caso=1;
  while(caso<=nCasos){
    cin >> C >> F >> X;
    cout << "Case #" << caso++ << ": ";
    cout << setprecision(7) << fixed  << solve() << endl;
  }
}
