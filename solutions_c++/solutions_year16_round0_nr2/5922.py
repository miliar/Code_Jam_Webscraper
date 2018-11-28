#include <iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream inputfile;
    ofstream outputfile;
    string fileName;
    int amount = 0;
    int amount1 = 1;
    string tempstring;
    int tickcount = 0;
    
    
    if ( argc == 2)
    {
        fileName = argv[1];
    }
    else 
    {
        cout << "Error - too many inputs" << endl;
        return 1;
    }
    
    inputfile.open(fileName.c_str(), ifstream::in);
    
    fileName.resize( fileName.size() - 3 );
    fileName = (fileName + ".out");
    
    outputfile.open(fileName.c_str(), ofstream::out);
    
    if (!inputfile.is_open()) 
    {
        cout << "Error - inputfile not opened." << endl;
        return 1;
    }
    if (!outputfile.is_open()) 
    {
        cout << "Error - outputfile not opened." << endl;
        return 1;
    }
    
    inputfile >> amount;
    while ( !inputfile.eof())
    {
        tickcount = 0;
        inputfile >> tempstring;
        for ( unsigned i = 0; i < tempstring.size() ; i++)
        {
            if ( i == 0 && tempstring.at(i) == 45)
            {
                while (i+1 < tempstring.size() && tempstring.at(i+1) == 45 )
                {
                    i++;
                }
                tickcount = tickcount + 1;
            }
            else if ( tempstring.at(i) == 45)
            {
                while (i+1 < tempstring.size() && tempstring.at(i+1) == 45 )
                {
                    i++;
                }
                tickcount = tickcount + 2;
            }
        }

        
        if ( amount1 <= amount)
        {
            outputfile << "Case #" << amount1 << ": " << tickcount << endl;
        }

        amount1 ++ ;

    }
    
    
    
    
    
    inputfile.close();
    outputfile.close();
    
    return 0;
}