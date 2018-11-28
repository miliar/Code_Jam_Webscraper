#include <iostream>
#include <fstream>

using namespace std;

long long gcd (long long a, long long b)
{
    long c;
    while(a != 0)
    {
        c = a;
        a = b%a;
        b = c;
    }
    return b;
}

int main(int argc, char *argv[])
{
    //Eingabe des Dateinamens über Konsole oder Übergabe als Eingabeparameter
    char* filename;
    if(argc > 1)
    {
        filename = argv[1];
    }
    else
    {
        char buffer[256];
        cout << "Input file name (up to 255 Characters): " << endl;
        cin >> buffer;
        filename = buffer;
    }
    
    int T = 0;
    
    try
    {
        ifstream datei(filename);
        if(!datei.is_open())
            throw 1;
        
        if(!datei.good())
            throw 2;
        datei >> T;
        if(T <= 0)
            throw 3;
        
        for(int k = 0; k < T; k++)
    {
        cout << "Case #" << k+1 << ": ";
        
        long long P, Q;
        datei >> P;
        char ba;
        datei >> ba;
        datei >> Q;
        
        //cout << P;
//        cout << " " << ba << " " << Q;
//        cin >> P;
        
        long long D = gcd(P, Q);
        
        P = P / D;
        Q = Q / D;
        //cout << P << "/" << Q;
        int result = 0;
        for(int i = 0; i < 40; i++)
        {
            //cout << P << "/" << Q << " ";
            if(Q == 1)
                break;
            if(result == 0 && 2*P >= Q)
            {
                result = i+1;
            }
            if(Q%2 != 0)
            {
                result = -1;
                break;
            }
            Q = Q/2;           
        }
        if(result == -1 || Q > 1)
        {
            cout << "impossible";
        }
        else
            cout << result;
        
        cout << endl;
    }
    }
    catch(int e)
    {
        cout << "Fehler (Nr. " << e << ") beim Einlesen der Datei.";
        int a;
    cin >> a;
        return 1;
    }
    
    //int a;
    //cin >> a;
    return 0;    
}
