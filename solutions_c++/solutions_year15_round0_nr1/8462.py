//
//  main.cpp
//  gcjQR15A
//
//
#include <iostream>
#include <fstream>

using namespace std;
int main(int argc, const char * argv[])
{
    
    ifstream read("/Users/Agnes/Documents/workspace/gcjQR15A/gcjQR15A/A-large.in", ios::in); // on ouvre lefichier en lecture
    
    ofstream write("/Users/Agnes/Documents/workspace/gcjQR15A/gcjQR15A/A-large.out", ios::out | ios::trunc);//déclaration du flux et ouverture du fichier
    
    int T;
    read >>T;
    cout <<T<<endl;
    
    int Smax;
    
    string car;
    int friends;
    int up;
    int si;
    
    for(int t=0; t<T; t++)
    {
        
        read >>Smax;
        read >>car;
        cout << Smax<<" "<<car<<endl;
        up = 0;
        friends=0;
        
        for(int i=0;i<=Smax;i++)
        {
            si =(car.at(i))-'0';
            if(si>0)
                if(up>=i)
                    up += si;
                else
                {
                    friends += i-up;
                    up += i-up+si;
                }
        }
        
        write << "Case #" << (t+1)<<": "<< friends<<endl;
        cout  << "Case #" << (t+1)<<": "<< friends<<endl;
    }
    
    
    return 0;
}

