#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    int cases, a, b, result;
    ifstream infile;
    ofstream outfile;
    infile.open("input.txt");
    outfile.open("answer.txt"); 
    
    infile >> cases;
    
    for (int j = 0; j < cases; j++)
        {
             result = 0;
             infile >> a >> b;
             cout << a << " " << b << endl;
             if( a == 1 && b >= 1)
                 result ++;
             if( a <= 4 && b >= 4)
                 result ++;
             if( a <= 9 && b >= 9)
                 result ++;
             if( a <= 121 && b >= 121)
                 result ++;
             if( a <= 484 && b >= 484)
                 result ++;
            outfile << "Case #" << j + 1 << ": " << result <<endl; 
        }
             
        
        
    system("PAUSE");
    return EXIT_SUCCESS;
}
