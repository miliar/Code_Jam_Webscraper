#include <cstdlib>
#include <iostream>
#include <iostream>
#include <fstream>

using namespace std;
unsigned long long n,m,i,j,k,t,a[11],T;

ofstream fout;
ifstream fin;
int main(int argc, char *argv[])
{   
    fin.open("ain2.txt",ios::in);
    fout.open("aout2.txt",ios::out);
    
    fin>>T;
    for(j=1;j<=T;j++)
    {   fin>>n;
        
        t=1;
        fout<<"Case #"<<j<<": ";
        if(n==0)
           fout<<"INSOMNIA"<<endl;
        else
        {  for(i=0;i<10;i++)
              a[i]=0;
           do
           {
             m=n*t;
             while(m!=0)
             {  
                 a[m%10]=1;
                 m=m/10;
             }
            
             k=0;
             for(i=0;i<10;i++)
               if(a[i]==0)
               {   
                   k=1;
                   break;
               }
             
             if(k==0)
             {
                 fout<<n*t<<endl;
                 break;
             }
              t++;
            }while(1);
        }
        
    }
    
    fin.close();
    fout.close();
    
    return EXIT_SUCCESS;
}
