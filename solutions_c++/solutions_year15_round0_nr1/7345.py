#include <iostream>
#include <fstream>
#include <cctype>
#include <string>

using namespace std;

int main()
{
    int test_cases=0;
    int Smax=0;
    string num_of_ppl;
    int counter=0;
    int invite=0;
    int total=0;
    ifstream fin;
    fin.open("A-large.in");
    fin>>test_cases;
    ofstream fout;
    fout.open("output.txt");
    while(counter<test_cases)
    {
    fin>>Smax;
    fin>>num_of_ppl;
    int i=1;
    char tempstr[7];
    tempstr[0]=num_of_ppl[0];
    int j=atoi(tempstr);
    total=0;
    invite=0;

      if(j==0)
     {
           invite++;
           total++;
     }
      else
          total=j;

   while(i<=Smax)
   {
    tempstr[0]=num_of_ppl[i];
    j=atoi(tempstr);
       if(i<=total)
       {
       total=total+j;
       }
       else
       {
           while(total<i)
           {
               invite++;
               total++;
           }
         total=total+j;     
       }
       i++;
   }
   fout<<"Case #"<<counter+1<<":"<<" " <<invite<<endl;
   counter++;
   }
    return 0;
}