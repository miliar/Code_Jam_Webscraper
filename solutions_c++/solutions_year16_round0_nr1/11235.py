#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <fstream>
using namespace std;

bool verificaVetor(bool v[],int n){
    for(int i=0;i<n;i++){
            if(v[i] == false){
                    return false;
            }
    }
    return true;
}


int main()
{
    int testes;
    int contTestes=1;
    int n;
    int aux;
    bool v[10];




    ifstream in;
    in.open("C://entrada1.in");
    ofstream out;
    out.open("C://saida1.txt");
    in >> testes;
    while(contTestes <= testes){
            in >> n;
            for(int i=0;i<10;i++){
                v[i] = false;
            }
            out << "Case " << contTestes << ": ";
            if(n == 0){
                    contTestes++;
                    out << "INSOMNIA" << endl;
            }
            else{
                    contTestes++;
                    aux = 1;


                    while(verificaVetor(v,10) == false){
                            int k = n*aux;

                            while(k > 0){
                                    v[k%10] = true;
                                    k = k/10;
                            }
                             aux++;
                    }
                    out << n*(aux-1) << endl;
            }


    }
    in.close();
    out.close();



    return 0;
}
