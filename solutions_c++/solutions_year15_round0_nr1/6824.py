#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>
#include <cstring>
#include <sstream>
using namespace std;

main () 
{
    const int SIZE = 1000000;
    char fileName[] = "A-large.in";
    char ch[SIZE];
    char *pch;
    int n, c, q, a, s;
    fstream file(fileName);
    ofstream file2;
    file2.open("sol.txt");
    
    file.getline(ch, SIZE);
    n = atoi(ch);
    
    for(int x=1; x<=n; x++)
    {
         a = 0;
         file.getline(ch, SIZE);
         pch = strtok(ch, " ");
         c = atoi(pch);
         
      //   cout << c << "\n";
         
         pch = strtok(NULL, " ");
         q = strlen(pch);
         s = q-1;
         int ov[q];
         string o;
         
         for(int i=0; i<q; i++)
         {
              o = pch[i];
              istringstream buffer(o);
              buffer >> ov[i];
              //cout << ov[i];
         }
       //  cout << "\n";
         s = 0;
         for(int i=0; i<c; i++)
         {
              a = a + ov[i];
              if(a < i+1)
              {
                   s++;
                   a++;
              }   
         }
         
         cout << s << "-" << c << "\n";
         
         file2 << "Case #" << x << ": ";
         
         if(s == 0)
         {
              file2 << "0";
         }
         else
         {
             file2 << s;
         }
         
         file2 << "\n";
         
         


    }
    
    file2.close();     
    getch();
}
