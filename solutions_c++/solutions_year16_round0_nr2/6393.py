#include <iostream>
#include <stdlib.h>
#include <fstream>
using namespace std;
int main()
{
    ifstream read("B-large.in");
    ofstream write("salida.txt");
    //cin.tie(0);
    //ios_base::sync_with_stdio(0);
    int casos;
    string caso;
    getline(read,caso);
    casos=atoi(caso.c_str());
    //cin>>casos;
    int respuesta;
    bool actual;
    for(int i=0;i<casos;i++)
    {
        //cin>>caso;
        getline(read,caso);
        respuesta=0;
        actual=caso[0]==43;
        //bool feliz[caso.size()];
        for(int j=1;j<caso.size();j++)
        {
            //feliz[j]=caso[j]==43;
            if((caso[j]==43)xor actual)
            {
                //cout<<"true"<<endl;
                respuesta++;
                actual=!actual;
            }
        }
            if((caso[caso.size()-1]==43)xor true) respuesta++;
            write<<"Case #"<<i+1<<": "<<respuesta<<endl;
            //cout<<"Case #"<<i+1<<" "<<respuesta<<endl;
    }
    write.close();
    return 0;
}
