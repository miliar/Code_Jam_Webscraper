#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("output.txt");
    int T,Smax,total,suma;
    string peo;
    in >> T;

    for(int x = 1 ; x <= T ; x++){
        total = 0;
        suma = 0;
        in >> Smax;
        int people[Smax+1];
        in >> peo;
        for(int i=0 ; i<=Smax ; i++){
            people[i] = ((int) peo[i]) - 48;
        }
        for(int i=1 ; i<=Smax ; i++){
            suma += people[i-1];
            if( i > suma){
                suma++;
                total++;
            }
        }

        out << "Case #";
        out << x;
        out << ": ";
        out << total << endl;
    }

    in.close();
    out.close();
    return 0;
}
