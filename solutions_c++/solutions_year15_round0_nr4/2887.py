#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;


int str2int(string s)
{
    stringstream ss;
    ss << s;
    int v;
    ss >> v;
    return v;
}

string d(int X, int R, int C)
{
    switch(X)
    {
        case 1:
            return "GABRIEL";
            
        case 2:
            if((R*C)%2 == 0)
                return "GABRIEL";
            else
                return "RICHARD";
                
        case 3:
            if((R*C)%3 == 0)
            {
                if(R==1 || C==1)
                    return "RICHARD";
                else
                    return "GABRIEL";  
            }
            else
                return "RICHARD";
                
        case 4:
            if((R*C)%4 == 0)
            {
                if(R==1 || C==1)
                    return "RICHARD";
                else if(R==2 || C==2)
                    return "RICHARD";
                else if(R==3 || C==3)
                    return "GABRIEL";  
                else
                    return "GABRIEL";
            }
            else
                return "RICHARD";
    
    }
       
    
    return "GABRIEL";
}

int main(int argc, char** argv)
{

    ifstream input;
    input.open(argv[1]);
    
    ofstream output;
    output.open(argv[2]);
    
    int testNumber;
    input >> testNumber;
    
    
    int X, R, C;
    string values;
    for(int i=1; i<=testNumber; ++i)
    {
        input >> X >> R >> C;
        output << "Case #" << i << ": " << d(X, R, C) << endl;
    }

    return 0;
}
