#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
   int t_cases, *smax, i, j, *count, t_count, people = 0, temp;
   string *audience;
   
   std::ofstream output;
   std::ifstream myfile;
   myfile.open ("A-small-attempt2.in");
   myfile >> t_cases;
   
   //cin >> t_cases;
   
   smax = new int[t_cases];
   count = new int[t_cases];
   audience = new string[t_cases];
   
   for( i = 0; i < t_cases; i++)
    {
        myfile >> smax[i];
        myfile >> audience[i];
        count[i] = 0;
    }
    myfile.close();
    
    for(i = 0; i < t_cases; i++)
    {
        j = 0;
        for ( string::iterator it=audience[i].begin(); it!=audience[i].end(); ++it)
        {
                temp = (int)(*it - '0');
               
               
              //  if(*it == '0')
               //     count[i]++;
                    
                if(temp)               
                {
                    if( j > people)
                    {    
                        count[i] += (j - people);
                        people += count[i];
                     }  
                }
                 j++;
                 people += temp;
        }
        cout <<count[i]<<"\n";
        people = 0;
    }
    
    output.open("res.txt");
    
    for(i = 0; i < t_cases; i++)
    {
        output << "case #"<< i+1 << ": " << count[i] <<"\n";
    }
    
    output.close();
   
   return 0;
}


