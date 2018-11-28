#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{

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
    
    long m_fair_square_array[1000];
    int m_fair_square_count = 0;
    
    // generate fair and squares!
    char ibuf[120];
    for(long count = 1; count < 1000; count++)
    {
             int limit = sprintf(ibuf, "%ld", count);
             char * ip = ibuf + limit - 1;
             char * op = ibuf;
             int pd = 1;
             for(int inner = 0; inner < limit; inner++)
             {
                     if( *ip-- != *op++)
                     {
                         pd = 0;
                         break;
                     }
             }
             if(pd)
             {
                 long test = count * count;
                 int limit = sprintf(ibuf, "%ld", test);
                 char * ip = ibuf + limit - 1;
                 char * op = ibuf;
                 int pd = 1;
                 for(int inner = 0; inner < limit; inner++)
                 {
                         if( *ip-- != *op++)
                         {
                             pd = 0;
                             break;
                         }
                 }
                 if(pd) m_fair_square_array[m_fair_square_count++] = test;
             }
         
    }
    
    
    int m_cases;
    input >> m_cases;
    
    for(int count = 0; count < m_cases; count++)
    {
         long min, max;
         input >> min >> max;
         int fcount = 0;
         for(int inner = 0; inner < m_fair_square_count; inner++)
         {
              if(m_fair_square_array[inner] >= min)
              {
                  if(m_fair_square_array[inner] > max) break;
                  fcount++;
              }  
         }
        output << "Case #" << count+1 << ": " << fcount << "\n";
    }
 
    system("PAUSE");
    return EXIT_SUCCESS;
}
