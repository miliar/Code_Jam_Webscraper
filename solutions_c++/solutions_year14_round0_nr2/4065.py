#include <iostream>
#include <fstream>
#include <conio.h>
#include <iomanip>


using namespace std;

int main()
{
    ifstream input("input.txt"); // Try to open a input file for reading 
    
    if(!input)
    {
           cout<<"Sorry !!!File named input.txt not opened\n";
           getch();     // Hold standard output terminal untill any key press
           return 0;
    }
    
    // Input file named input.txt opened for reading purpose
    
     ofstream output("output.txt");   // Try to open a output file for writing
     
     if(!output)
     {
           cout<<"Sorry !!!File named output.txt not opened\n";
           getch();     // Hold standard output terminal untill any key press 
           return 0;
     }
    
    // Output file named output.txt opened for writing purpose

    int T;
    input >> T;
    
    int M = T;
    
    while(T--)
    {
        double C, F, X;
        input >> C;
        input >> F;
        input >> X;
        double d1 = 2.0, d2 = 2.0 + F;
        double t1 = (C/d1) + (X/d2);
        double t2 = (X/d1);
        double time = 0.0;
        while(t1 < t2)
        {
           time = time + (C/d1);
           d1 = d1 + F;
           d2 = d2 + F;
           t1 = (C/d1) + (X/d2);
           t2 = (X/d1);
        }
        time = time + (X/d1);
        output.precision(7);
        output.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed
        output <<"Case #"<<M-T<<": "<<time << endl;
    }
        
    input.close();      // Close input stream of reading
   
    output.close();     // Close output stream of writing

    return 0;
}
