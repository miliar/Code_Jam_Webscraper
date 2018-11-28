#include <iostream>
#include <list>

using namespace std;

int deceive(list<double> &Naomi, list<double> &Ken){

    if(Naomi.front() > Ken.front()){
        Naomi.pop_front();
        Ken.pop_front();
        if(!Naomi.empty()) return 1 + deceive(Naomi, Ken);
        else return 1;
    }else{
        Naomi.pop_front();
        Ken.pop_back();
        if(!Naomi.empty()) return deceive(Naomi, Ken);
        else return 0;
    }

}

int war(list<double> &Naomi, list<double> &Ken){

    if(Naomi.back() > Ken.back()){
        Naomi.pop_back();
        Ken.pop_front();
        if(!Naomi.empty()) return 1 + war(Naomi, Ken);
        else return 1;
    }else{
        Naomi.pop_back();
        Ken.pop_back();
        if(!Naomi.empty()) return war(Naomi, Ken);
        else return 0;
    }

}

int main(){

    int testes, casos = 1, pecas;
    double aux;

    cin >> testes;

    for(int i = 0; i < testes; i++){
        cin >> pecas;
        list<double> Naomi, Ken;

        for(int j = 0; j < pecas; j++){
            cin >> aux;
            Naomi.push_back(aux);
        }

        for(int j = 0; j < pecas; j++){
            cin >> aux;
            Ken.push_back(aux);
        }

        Naomi.sort();
        Ken.sort();
        list<double> Naomi2 (Naomi);
        list<double> Ken2 (Ken);

        cout << "Case #" << casos << ": " << deceive(Naomi, Ken) << " " << war(Naomi2, Ken2)<<endl;
        casos++;

    }

    return 0;
}
