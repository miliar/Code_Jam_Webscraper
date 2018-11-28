#include <iostream>

using namespace std;

int main()
{
    int numCases;
    double C,F,X;

    cout << std::fixed;
    cout.precision(7);

    cin >> numCases;
    for (int numCase=0 ; numCase<numCases ; numCase++)
    {
        cin >> C ;
        cin >> F ;
        cin >> X ;

//        cout << C << " " << F <<" " << X << endl;

        double tiempoGlobal = 0.0;
        double velocidad = 2.0;
        double proxFarm = C/velocidad;
        double tiempoMeta = X/velocidad;
        double tiempoTotal =tiempoGlobal + tiempoMeta;
        double tiempoTotalAnterior;
        do{
            tiempoTotalAnterior = tiempoTotal;
            tiempoGlobal += proxFarm;
            velocidad+=F;
            proxFarm = C/velocidad;
            tiempoMeta=X/velocidad;
            tiempoTotal=tiempoMeta+tiempoGlobal;

//            cout << tiempoGlobal << " " <<
//                velocidad << " " <<
//                proxFarm << " " <<
//                tiempoMeta << " " <<
//                tiempoTotal << " " <<
//                endl;
        }
        while(tiempoTotal<tiempoTotalAnterior);

        cout << "Case #" << numCase+1 << ": " << tiempoTotalAnterior <<endl;
    }

    return 0;
}
