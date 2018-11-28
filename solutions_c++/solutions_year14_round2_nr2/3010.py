#include <iostream>
#include <fstream>
#include <conio.h>

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
          long A, B, K;
          input >> A;
          input >> B;
          input >> K;
          int count = 0;
          for(int i = 0; i < A; i++)
          {
              for(int j = 0; j < B; j++)
              {
                   if((i & j) < K)
                         count++;
              }
          }
          output<<"Case #"<<M-T<<": "<<count<<endl;
    }
        
    input.close();      // Close input stream of reading
   
    output.close();     // Close output stream of writing
    
    return 0;
}
