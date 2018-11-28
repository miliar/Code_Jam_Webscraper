#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main(){
    ofstream cout("b.txt");
    cout.precision(7);

    int casos,ca=1;
    cin>>casos;
    while(casos--){
        double c,f,x,ttotal=0;
        double produccion=2;
        cin>>c>>f>>x;
        bool continuar=true;
        while(continuar){
            double tiempo=x/produccion;
            double tcomprar= c/produccion;
            double total=tcomprar+ x/(produccion+f);
            //cout<<"tiempo: "<<tiempo<<" total: "<<total<<" ttotal: "<<ttotal<<" produccion" <<produccion<<endl;
            if(tiempo<=total){
                continuar=false;
                ttotal+=tiempo;
            }else{
                produccion+=f;
                ttotal+=tcomprar;
            }
        }
        cout<<"Case #"<<ca<<": "<<setprecision(7)<<fixed<<ttotal<<endl;;
      ca++;
    }
}
