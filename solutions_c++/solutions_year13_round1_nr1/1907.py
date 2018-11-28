#include <iostream>
#include <fstream>

using namespace std;

int load(unsigned long long int r[],unsigned long long int t[])
{
    int cases;
    
    ifstream input;
    input.open("input.in");
    if(input.is_open())
    {
          input >> cases;
          cout << "Cases: " << cases <<endl;
          for(int i=0;i<cases;i++)
          {
              input >> r[i] >> t[i];
          }
          input.close();
          return cases;
    }
    else
    {
          cout << "There is no such file" << endl;
          input.close();
          return -1;
    }    
}

bool save(int cases, unsigned long long int count[])
{
     ofstream output;
     output.open("output.txt");
      
     if(output.is_open())
     {
         for(int i=0; i<cases; i++)
         {
               output << "Case #" << i+1 << ": "<< count[i] << endl;
         }
         output.close();
     }
     else
     {
          cout << "File can' t open for save." << endl;
          output.close();
          return -1;
     }
}


main()
{
      int cases; 
      unsigned long long int r[6000], t[6000], j;
      cases = load(r,t);
      unsigned long long int count[cases];
      for(int i=0; i<cases; i++)
      {
           count[i] = 0;
      }
      for(int i=0; i<cases; i++)
      {              
           do
           {
               //cout << "t " << t[i] << " res " <<(2*r[i]+1) << endl;
               if(t[i]>=(2*r[i]+1))
                  t[i] -= (2*r[i]+1);
               else
                  break;
                  //cout << r[i] << endl;
               r[i]+=2;
               //cout << r[i] << endl;
               //system("pause");
               count[i]++;
           }while(t[i]>=0);
           //count[i]--;
           cout << i << endl;
      }
      
      save(cases,count);
      system("pause");
      
}

