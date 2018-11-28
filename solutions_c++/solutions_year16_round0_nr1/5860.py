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
    int tempnum = 0;
    int tempnum1 = 0;
    int tempnum2 = 0;
    int j = 0;
    int k = 0;
    int l = 0;
    
    
    vector <int> vec (10, 0);
    
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
        
        inputfile >> tempnum;
        l = 0;
        k = 0;
        
        while ( k == 0)
        {
            l++;
            tempnum1 = tempnum * ( l );
            tempnum2 = tempnum1;
            while ( tempnum1 > 0)
            {
                j = tempnum1 % 10;
                vec.at(j) = 1;
                tempnum1 = tempnum1 / 10;
            }
            
            
            k = 1;
            for ( unsigned int z = 0; z < vec.size(); z++)
            {


                if( vec.at(z) == 0)
                {
                    k = 0;
                }
            }
            
            if ( tempnum == 0)
            {
                k = 1;
            }
            
        }
        
        if ( tempnum != 0 && amount1 <= amount)
        {
            outputfile << "Case #" << amount1 << ": " << tempnum2 << endl;
        }
        else if (amount1 <= amount)
        {
            outputfile << "Case #" << amount1 << ": INSOMNIA" << endl;
        }
        
        amount1 ++ ;
        for ( unsigned int z = 0; z < vec.size(); z++)
            {
                vec.at(z) = 0;
            }
    }
    
    
    
    
    
    inputfile.close();
    outputfile.close();
    
    return 0;
}