//code2323
//Problem D : Ominous Omino
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    int T, X,R,C;
    bool B;
    
    ifstream infile;
    ofstream file2;
    
    
    char filename[30];
    char ch;
    cout<<"Please enter file name"<<endl;
    cin>>filename;
    infile.open(filename);
    file2.open("OutputFile.txt");
    
    if(!infile)
    {
        cout<<"File not found."<<endl;
        return 1;
        
    }
    infile >> T;
    
    for (int i = 0; i < T; i++)
    {
        infile >> X >> R >> C;
        if (X == 1)
        {
            B = 1;
        }
        else if ((X>R) && (X>C))
        {
            B = 0;
        }
        else if (X == 2)
        {
            if (((R*C) % 2)==0)
            {
                B = 1;
            }
            else
            {
                B = 0;
            }
        }
        else if (X == 3)
        {
            if ((((R*C) % 3) == 0) && ((R != 1) && (C!=1)))
            {
                B = 1;
            }
            else
            {
                B = 0;
            }
        }
        else if (X == 4)
        {
            if ((R < 3) || (C < 3))
            {
                B = 0;
            }
            else
            {
                B = 1;
            }
        }
        file2 << "Case #" << i + 1 << ": ";
        if (B == 0)
        {
            file2 << "RICHARD" << endl;
        }
        else
        {
            file2 << "GABRIEL" << endl;
        }
    }
    
    return 0;
}