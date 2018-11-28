#include <iostream>
#include <set>
#include <fstream>
using namespace std;

int main(){
    int casos,fichas;
    ofstream cout("war.txt");
    cin>>casos;
    int c=1;
    while(casos--){
        cin>>fichas;
        set<double> naomi,ken,copia;
        double peso;
        for(int i=0;i<fichas;i++){
            cin>>peso;
            naomi.insert(peso);
        }
        for(int i=0;i<fichas;i++){
            cin>>peso;
            ken.insert(peso);
        }
        set<double>::iterator it= naomi.begin();
        set<double>::iterator it2;
        copia=ken;
        int puntosw=0;
        for(;it!=naomi.end();it++){
            it2=ken.begin();
            while(*it > *it2 && it2!= ken.end()){
                it2++;
            }
            if(it2==ken.end()){
                ken.erase(ken.begin());
                puntosw++;
            }else{
                ken.erase(it2);
            }
        }
        int puntosdw=0;
        set<double>::reverse_iterator it3;
        while(naomi.size()>0){
            it3=copia.rbegin();
            it=naomi.begin();
            it2=copia.begin();
            bool descartando=false;
            for(;it!=naomi.end();it++){
                if(*it < *it2){
                    descartando=true;
                    break;
                }
                it2++;
            }
            it=naomi.begin();
            if(descartando){
                if((*it) < (*it3)){
                naomi.erase(*it);
                copia.erase(*it3);
                }else{
                    break;
                }
            }else{
                break;
            }


        }
        puntosdw+=naomi.size();
        cout<<"Case #"<<c<<": "<<puntosdw<<" "<<puntosw<<endl;
        c++;
    }
    cout.close();
    return 0;
}
