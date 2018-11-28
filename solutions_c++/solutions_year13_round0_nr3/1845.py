#include<iostream>
#include<algorithm>
#include<functional>
#include<cmath>
#include<math.h>
#include<string.h>
#include<string>
#include<fstream>
using namespace std;
long long int a[1001];
int main ()
{     long long int i,j,k,l,n,m,p,t,q,o=0;
   long long int c[100];
   //ofstream fout;
       // fin.open("Input.txt");
       // fout.open("Output.txt");
       for(i=1; i<=10000005; i++)
       {  n=i; k=0;
          while(n>0)
          {
                    c[k++]=n%10;
                    n=n/10;
          }
          p=0; q=k-1;
          while(c[p]==c[q])
          {
                           p++;
                           q--;
          }
          if(p>q)
          {
                  k=0;
                  n=i*i;
                  while(n>0)
                  {
                    c[k++]=n%10;
                    n=n/10;
                  }
                     p=0; q=k-1;
                  while(c[p]==c[q])
                   {
                           p++;
                           q--;
                   }
                   if(p>q)
                   a[o++]=i*i;
          }
       }            
        // for(i=0; i<o; i++)
        // fout<<a[i]<<",";          
        ifstream fin;
        ofstream fout;
        fin.open("Input.txt");
        fout.open("Output.txt");
        fin>>n;
        q=1;
        while(q<=n)
        {          p=0;
                   fin>>m>>k;
                   for(i=0; i<=40; i++)
                   if(a[i]>=m&&a[i]<=k)
                   p++;
                   fout<<"Case #"<<q<<": ";
                   fout<<p<<"\n";
                   q++;
        }
fin.close();
fout.close();

//system("pause");
}
