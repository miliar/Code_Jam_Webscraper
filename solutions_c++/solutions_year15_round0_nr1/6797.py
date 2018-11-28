#include <iostream>
#include <fstream>

using namespace std;


int main (){
int casos, i;
int max, solu; 
char vector[1000], buff;
fstream archivoin("D-small-practice.in");
fstream archivoout("D-small-practice.out");

if((archivoin)&&(archivoout)){
    archivoin >> casos;
    for(i=0;i<casos;i++){
        solu=0;
        archivoin >> max;
        //archivoin >> buff;
        for (int i =0;i<=max;i++){
            archivoin >> vector[i];  
			cout << vector[i] << endl;
        }
        int asistentes=vector[0]-48;
        cout << max << "fin" << endl;
        for (int i=1;i<=max;i++){
            if(asistentes >= i)asistentes+=(vector[i]-48);
            else {
                 asistentes++;
                 solu ++;
                 i--;
                 }
        }
        
        archivoout << "Case #"<< i+1 << ": ";
        archivoout << solu;
        if(i!=casos-1) archivoout << endl;
    }
    archivoin.close();
    archivoout.close();
} else cout << "No se pudo abrir el archivo" << endl;

system("PAUSE");
return 0;
}
