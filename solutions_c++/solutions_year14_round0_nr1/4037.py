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
           int F;
           input >> F;
           int Data1[4];
           int dump;
           int rem = 4 - F;
           while(F--)
           {
               for(int i = 0; i < 4; i++)
                       input >> Data1[i];
           }
           while(rem--)
           {
               for(int i = 0; i < 4; i++)
                       input >> dump; 
           }
           int S;
           input >> S;
           int Data2[4];
           rem = 4 - S;
           while(S--)
           {
               for(int i = 0; i < 4; i++)
                       input >> Data2[i];       
           }
           
           while(rem--)
           {
               for(int i = 0; i < 4; i++)
                       input >> dump; 
           }
           int count = 0, num;
           for(int i = 0; i < 4; i++)
           {
             for(int j = 0; j < 4; j++)
             {
                if(Data1[i] == Data2[j])
                {
                   num = Data1[i];
                   count++;
                }
             }
           }

           if(count == 0)
              output<<"Case #"<<M-T<<": Volunteer cheated!"<<endl;
           else if(count == 1)
              output<<"Case #"<<M-T<<": "<<num<<endl;
           else
               output<<"Case #"<<M-T<<": Bad magician!"<<endl; 
                
         
    }
        
    input.close();      // Close input stream of reading
   
    output.close();     // Close output stream of writing
    return 0;
}
