#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    string strA, strB;
    int T;
    int limInf, limSup, aux, aux2;
    double temp;
    stringstream i2s;
    int total;
    
    while(cin >> T)
    {
        for(int cont = 1; cont <= T; cont++)
        {
            cin >> limInf;
            cin >> limSup;
            total = 0;
            for(limInf; limInf <= limSup; limInf++)
            {
                temp = sqrt(limInf);
                aux2 = temp;
                temp -= aux2;
                if(temp > 0) continue;
                
                // Faz a operação com o número
                strA = ""; // Limpa as strings
                strB = "";
                i2s.str(""); // Limpa o stream
                aux = limInf;
                i2s << aux;
                strA = i2s.str();
                strB = string(strA.rbegin(), strA.rend());
                if(strA.compare(strB) != 0) continue;
                
                // Faz a operação com o quadrado do número
                strA = ""; // Limpa as strings
                strB = "";
                i2s.str(""); // Limpa o stream
                i2s << aux2;
                strA = i2s.str();
                strB = string(strA.rbegin(), strA.rend());
                if(strA.compare(strB) != 0) continue;
                
                total++;
            } 
            
            cout << "Case #" << cont << ": " << total << endl; 
        }  
    }
    return 0;    
}
