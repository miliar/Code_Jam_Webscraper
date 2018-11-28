#include <iostream>

using namespace std;
void caso(){
    double C,F,X;
    cin >> C >> F >> X;
    int pasos = ((F*X-2.0*C)/(C*F));
    double total =0.0;
    if(pasos < 0 ) pasos = 0;
    for(int i =0;i<pasos;i++){
        total += C/(2.0+i*F);
    }
    double respuesta =total+X/(2+pasos*F);
    //cout << respuesta << endl;
    total += C/pasos;
    total += X/(2+(pasos+1)*F);
    if(respuesta > total){
        respuesta = total;
    }

    cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
    cout.precision(7);
    cout << respuesta << endl;
    //cout.setprecision(7);
    //cout << std::fixed   << respuesta << endl;
}
int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        cout << "Case #" << i << ": ";
        caso();
    }
    return 0;
}
