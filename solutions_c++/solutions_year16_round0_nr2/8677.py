#include <set>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

int main()
{

    char t[10];
    ifstream f;
    f.open("c:\\input.txt");
    f.getline(t,10);

    ofstream o;
    o.open("c:\\output.txt");
    char out[100];
    int i = atoi(t);
    
    for(int k=1; k<=i;k++)
    {
        char str[105]; 
        f.getline(str, 105);
        int sz = strlen(str);
        int count=0;       
                
           for(int x=sz-1; x>=0; x--)
           {
               if(str[x] == '-')
               {
                   //flip all the above
                   str[x] = '+';
                   for(int y=0; y<x; y++)
                   {
                       if(str[y] == '-')
                           str[y] = '+';
                       else if(str[y] == '+')
                           str[y] = '-';
                   }
                   count++;
               }
           }
                 
        
        sprintf(out, "Case #%d: %d\n", k, count);
        o << out;
    }

    f.close();
    o.close();
    return 0;
}
