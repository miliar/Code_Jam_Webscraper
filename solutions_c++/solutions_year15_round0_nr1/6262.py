#include <iostream>
#include <cstdlib>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("input.txt");
    ofstream of("output.txt");
    int qwe;
    in>>qwe;
    int num;
    int vett[1005];
    char vett2[1005];
    for(int qwerty=0;qwerty<qwe;qwerty++)
    {
            int cont=0;
            in>>num;
            for(int i=0;i<=num;i++)
               in>>vett2[i];
            
            for(int i=0;i<=num;i++)
              {
                vett[i]=(int)(vett2[i]-'0');
              }
            
            for(int i=0;i<=num;i++)
            {
               while(vett[i]>1)
                 {
                   vett[i+1]++;
                   vett[i]--;
                 }
                
            }
            
            for(int i=0;i<num;i++)
               {
                    if(vett[i]==0)
                    cont++;  
               }
    of<<"Case #"<<qwerty+1<<": "<<cont<<"\n";
    } 
}
