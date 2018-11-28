#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
   int cases, n, curN, k;
   int curCase = 1;
   bool uniques[10];
   bool unique;
   string nString;
   ifstream fin;
   ofstream fout;
   fin.open("input.txt");
   fout.open("output.txt");

   fin>>cases;
   while(curCase <= cases)
   {
       fin>>n;
	   curN = n;
       if (n == 0)
       {
            fout<<"Case #"<<curCase<<": INSOMNIA"<<endl;
            curCase++;
            continue;
       }

       nString = to_string(n);
       unique = false;
       
       for(k = 0; k < 10; k++)
            uniques[k] = 0;
       
       while (!unique)
       {
           for(k = 0; k < nString.length(); k++)
           {
                uniques[nString[k] - 48] = 1;
           }
           
           for(k = 0; k < 10; k++)
           {
                if(uniques[k] != 1)
                    break;
           }
           if(k == 10)
           {
                unique = true;
                break;    
           }
        
           curN += n;
           nString = to_string(curN);
       }

       if(unique)
            fout<<"Case #"<<curCase<<": "<<curN<<endl;
       else
            fout<<"Case #"<<curCase<<": INSOMNIA"<<endl;
       curCase++;
   }
   
   
   return 0;
}