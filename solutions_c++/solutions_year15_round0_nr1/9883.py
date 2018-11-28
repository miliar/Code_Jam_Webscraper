#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(void)
{
    string cadena,aux;
    ifstream entrada;
    ofstream salida;
    int t,i,j,ultimo,num,audien,cont,need;

    entrada.open("A-small-attempt6.in",ios::in);
    salida.open("Output.in",ios::out);

    getline(entrada,cadena,'\n');
    t=atoi(cadena.c_str());
    j=1;
    while(getline(entrada,cadena,'\n')){
        cout<<cadena<<endl;
        audien=0;
        need=0;
        for(i=2;i<9;i++){
            if(!cadena[i])
                break;
            aux=cadena[i];
            num=atoi(aux.c_str());
            if(i==2){
                audien=audien+num;
            }else if(audien<(i-2)&&num>0){
                need=need+((i-2)-audien);
                audien=audien+need+num;
            }else if(audien>=(i-2)){
                audien=audien+num;
            }
        }
        cout<<"Case #"<<j<<": "<<need<<endl;
        salida<<"Case #"<<j<<": "<<need<<endl;
        j++;
    }
    entrada.close();
    salida.close();
    return 0;
}
