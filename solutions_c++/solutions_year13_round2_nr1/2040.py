#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

double Iteration(double N, double R, double P)
{
       double top = 2*N*N + 2*R*N - N - P;
       double bottom = 4*N + 2*R - 1;
       return top / bottom;
}

int main(int argc, char *argv[])
{
    long long motes[101]; // upto 100 motes
    
    if(argc < 3)
    {
            cout << "Oops - not enough command line parameters\n\n";
            system("PAUSE");
            return EXIT_FAILURE;
    }   
    
    ifstream input;
    input.open(argv[1]);
    
    ofstream output;
    output.open(argv[2]);
    
    int m_cases;
    input >> m_cases;
    
    for(int cases = 0; cases < m_cases; cases++)
    {
        long long armins;
        int existing;
        input >> armins >> existing;
        
        // read the exisiting into an ordered array!
        
        for(int count = 0; count < existing; count++)
        {
           long long mote;
           input >> mote;
           if(!count) motes[count] = mote;
           else
           {
               // see where it fits
               int inserted = 0;
               long long shift;
               for(int inner = 0; inner < count; inner++)
               {
                       if(!inserted)
                       {
                           if(mote <= motes[inner])
                           {
                                   inserted = 1;
                                   shift = motes[inner];
                                   motes[inner] = mote;
                           }
                       }
                       else
                       {
                           long long smote = motes[inner];
                           motes[inner] = shift;
                           shift = smote;
                       }    
               }
               if(!inserted)
               {
                   motes[count] = mote;
               }
               else
               {
                   motes[count] = shift;
               }   
           }     
        }
        // get here and all is in ascending order....
        long long activties = 0;
        if(armins == 1)
        {
                  activties = existing;
        }
        else
        {
            for(int count = 0; count < existing; count++)
            {
                    if((armins <=  motes[count]) && ((count+1) == existing))
                    {
                        activties++; // delete!
                        break;      
                    }
                    while(armins <=  motes[count])
                    {
                        armins += armins - 1; // we always insert the largest we can
                        activties++;          
                    }
                    armins +=  motes[count]; // eat the sub particle
            }
        }
        if(activties > existing) activties = existing; // doh!
       output << "Case #" << cases+1 << ": " << activties << "\n";
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
