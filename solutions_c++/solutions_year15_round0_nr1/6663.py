#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
int unsigned T,aux,cantidad;
    int long long unsigned total,amigos;
    char entrada[1050];
    char a;
    cin >>T;
    aux=T;
    while(T--){
        total=0;
        amigos=0;
        cin >>cantidad>> entrada;
        for (int i=0; i<=cantidad;i++){
            if (total<i){
               amigos+=i-total;
                total=i;
            }
            a=entrada[i];
            total+= atoi(&a);
        }

    cout <<"Case #"<<aux-T<<": "<<amigos<<endl;
    }
    return 0;
}
