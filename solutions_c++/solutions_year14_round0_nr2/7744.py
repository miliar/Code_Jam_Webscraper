#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main ()
{
    int cases;
    double C, F, X, OldC, OldX, NewC, NewX, rate;
    ifstream in;
    ofstream out;
    in.open("Input.txt");
    out.open("output.txt");
    
    if(in.is_open())
    {
    in >> cases;
    for(int i=0; i<cases; i++)
    {
            out << "Case #" << i+1 << ": ";
            rate = 2;
            in >> C >> F >> X;
    
            OldC = C/2;
            OldX = X/2;
            rate=rate+F;
    
            while(1)
            {
                    NewC = OldC + (C/rate);
                    NewX = OldC + (X/rate);
                    if(NewX >= OldX)
                    break;
                    else
                    {
                        OldC = NewC;
                        OldX = NewX;
                        rate = rate+F;
                    }
            }
            out << setprecision(9) << OldX << endl;
    }
    }//end if
    else
    out << "Cannot open file!" << endl;
    return 0;
}
