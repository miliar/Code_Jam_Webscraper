#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int m[6][6];
    bool mark[20];
    int t,col;
    ofstream myfile;
    ifstream lectura;
    myfile.open("salida3.txt");
    lectura.open("A-small-attempt0.in");
    lectura >> t;
    for(int kase = 0 ; kase<t ; kase++){
        lectura >> col;
        for(int i=1;i<=16;i++)
            mark[i] = false;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                lectura >> m[i][j];
        for(int i=1;i<=4;i++)
            mark[m[col][i]] = true;
        int cont=0;
        lectura >> col;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                lectura >> m[i][j];
        
        for(int i=1;i<=4;i++)
            if(mark[m[col][i]] == true)
                cont++;
        
        if(cont == 0)
            myfile << "Case #" << kase+1 << ": Volunteer cheated!" << endl;
        else
            if(cont > 1)
                myfile << "Case #" << kase+1 << ": Bad magician!" << endl;
            else
                for(int i=1;i<=4;i++)
                    if(mark[m[col][i]] == true)
                        myfile << "Case #" << kase+1 << ": " << m[col][i] << endl;
        
    }
}