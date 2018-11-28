#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

void solve(int CASE);

int main() {
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w+",stdout);
    int T; cin>>T;
    for (int c = 1;c <= T;c++){
        solve(c);
    }
}
void solve(int CASE){
    int N; cin>>N;
    vector <int> datos;
    for (int c = 0;c < N;c++){
        int value; cin>>value;
        datos.push_back(value);
    }
    int a = 0;
    int per_10second = 0;
    for (int d = 0;d < datos.size()-1;d++){
        if (datos[d] > datos[d+1]){ //si faltan hongos
            int difference = datos[d] - datos[d+1];

            a += difference;
            if ( difference > per_10second ){
                per_10second = difference;
               // cout<<per_second<<endl;
            }
        }
    }
    double b = 0; //per_second * (datos.size()-1) * 10;

    for (int d = 0;d < datos.size()-1;d++){

        if (datos[d] < per_10second){ //si no da el intervalo para lo que voy a comer
            b += datos[d];
            //cout<<datos[d]<<endl;
        }else{
            b += per_10second;
            //cout<<per_second*10<<endl;
        }
    }
    cout<<"Case #"<<CASE<<": "<<a<<" "<<b<<endl;//<<" "<<b<<endl;
}