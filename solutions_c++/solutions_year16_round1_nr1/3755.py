#include <iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;



int main(int argc, char *argv[])
{
    ifstream inputfile;
    ofstream outputfile;
    string fileName;
    std::string tempstring;
    std::string newstring;
    
    int amount = 0;
    int amount1 = 1;

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
    std::string cahrac;
    std::string noob;
    
    while ( !inputfile.eof() && amount1 <= amount)
    {
        inputfile >> tempstring;
        newstring.clear();
        newstring.push_back(tempstring.at(0));
        
        
        
        for ( unsigned i = 1; i < tempstring.size(); i++)
        {
            
            if ( tempstring.at(i) >= newstring.at(0))
            {
                // newstring.push_back(' ');
                // for ( unsigned j = newstring.size() -2; j >=0; j--)
                // {
                //     newstring.at(j+1) = newstring.at(j+1);
                // }
                // newstring.at(0) = tempstring.at(i);
                
                newstring.insert(newstring.begin(), tempstring.at(i) );
            }
            else 
            {
                newstring.push_back(tempstring.at(i));
            }
        }
        
            
        outputfile << "Case #" << amount1 << ": " <<
        newstring << endl;
                
            
        
        
        
        
        amount1 ++;
    }
    
    
    
    // cout << tempnum << endl;
    // cout << tempnum1 << endl;
    
    inputfile.close();
    outputfile.close();
    
    return 0;
}