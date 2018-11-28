#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream ent;
    ofstream sal;
    ent.open("B-small-attempt0.in");
    sal.open("salida.txt");
    int a,b,k;
    long long cont = 0;
    int c;
    ent >> c;

    for(int xxx=0; xxx < c ; xxx++) {
        ent >> a >> b >> k;
        for(int i=0;i<a;i++) {
            for(int j=0;j<b;j++){
                if((i&j) < k)
                {
                    cont++;
                    
                }
            }
        }
        sal << "Case #" << xxx+1 << ": " << cont << endl;
        cont = 0;
    }
    ent.close();
    sal.close();

}