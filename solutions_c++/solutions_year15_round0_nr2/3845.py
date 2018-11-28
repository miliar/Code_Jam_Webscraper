#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

void Solve(int c);
int Avanzar(int elec , int mov , vector <int> platos);
void show(vector <int> valores);

int main() {
    freopen("B-small-attempt15.in","r",stdin);
    freopen("B-small-attempt15-output.out","w+",stdout);

    int T; cin>>T;
    for (int x = 1;x <= T;x++){
        Solve(x);
    }
}
bool compare(int a,int b){
    return a > b; //de mayor a menor
}

void Solve(int c){
    cout<<"Case #"<<c<<": ";

    int D; cin>>D;

    vector <int> platos;
    for (int x = 0;x < D;x++){
        int valor; cin>>valor;
        platos.push_back(valor);
    }
    //how(platos);

    //genero dos posibilidades
    int a = Avanzar(0,0,platos);
    int b = Avanzar(1,0,platos);
    //muestro la mejor

    cout<<min(a,b)<<endl;
}

vector <int> Reducir(vector <int> val){
    for (int x = 0;x < val.size();x++){
        val[x] --;
    }
    return val;
}
vector <int> Mover(vector <int> val,int mover){

    val[0] -= mover; //le sacamos la mitad al mas grande
    val.push_back( mover ); //se la ponemos a un plato nuevo

    return val;
}
void show(vector <int> valores){
    cout<<"{";
    for (int x = 0;x < valores.size();x++){
        cout<<valores[x]<<" ";
    }
    cout<<"}"<<endl;
}
int Avanzar(int elec , int mov , vector <int> platos){ //devuelve la cantidad de movimientos que se hicieron

    sort(platos.begin() , platos.end() , compare);

    //show(platos);
    if (platos[0] < 3){ //si el plato mayor es 1 o 2, entonces da lo mismo esperar o mover platos
        return mov + platos[0]; //devolvemos como si esperaramos los turnos para que todos coman
    }

    /*** Ejecuto las dos instrucciones, segun la que coresponda ***/
    vector <int> siguiente;

    int mejor = 1e9; //las dos posibilidades

    if (elec == 0){ //comer
        siguiente = Reducir(platos);
        mov ++; //agrego ese movimiento

        /*** Genero las dos posibilidades ***/
        int a = Avanzar(0 , mov , siguiente); //diciendole a la proxima que espere
        int b = Avanzar(1 , mov , siguiente); //diciendole a la proxima que mueva
        mejor = min(a,b); //guardo la mejor

    }else if (elec == 1){ //mover
        /*** Por cada cantidad de panqueques a mover ***/

        mov ++; //agrego el movimiento

        for (int c = 2;c <= platos[0]/2;c++) {
            /*** Muevo el plato 0 c unidades ***/
            siguiente = Mover(platos, c);

            /*** Genero la posibilidad ***/
            int p = Avanzar(0 , mov , siguiente);
            int w = Avanzar(1 , mov , siguiente);

            /*** Reviso si es menor a la mejor ***/
            int b = min(p,w);
            mejor = min(mejor,b);
        }
    }

    /*** Devuelvo la mejor ***/
    return mejor;
}