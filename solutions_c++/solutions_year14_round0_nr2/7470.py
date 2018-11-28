#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main ()
{
    int cases;
    double C, F, X, PreviousC, PreviousX, NewC, NewX, rate;
    ifstream infile;
    ofstream outfile;
    infile.open("Input.txt");
    outfile.open("output.txt");
    
    if(infile.is_open())
    {
    infile >> cases;
    for(int i=0; i<cases; i++)
    {
            outfile << "Case #" << i+1 << ": ";
            rate = 2;
            infile >> C >> F >> X;
    
            PreviousC = C/2;
            PreviousX = X/2;
            rate=rate+F;
    
            while(1)
            {
                    NewC = PreviousC + (C/rate);
                    NewX = PreviousC + (X/rate);
                    if(NewX >= PreviousX)
                    break;
                    else
                    {
                        PreviousC = NewC;
                        PreviousX = NewX;
                        rate = rate+F;
                    }
            }
            outfile << setprecision(9) << PreviousX << endl;
    }
    }//end if
    else
    outfile << "Cannot open file!" << endl;
    return 0;
}
