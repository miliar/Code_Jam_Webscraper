#include<iostream>
#include<algorithm>
#include<functional>
#include<cmath>
#include<math.h>
#include<string.h>
#include<string>
#include<fstream>
using namespace std;
int main ()
{     int i,j,k,l,n,m,p,t,q,f,y;
       ifstream fin;
       ofstream fout;
      fin.open("Input.txt");
      fout.open("Output.txt");
      fin>>n;
      q=1;
      while(q<=n)
      {
                 fin>>m>>k;
                 int a[m][k];
                 for(i=0; i<m; i++)
                  for(j=0; j<k; j++)//{
                   fin>>a[i][j];
                   //cout<<a[i][j];}
                   
                   for(i=0; i<m; i++)
                   {
                    for(j=0; j<k; j++)
                    {         f=0;
                             l=a[i][j];
                              y=0;
                              for(p=0; p<m; p++)
                              y=max(y,a[p][j]);
                              if(l==y)
                               f=1;
                               y=0;
                               if(f==0)
                               {
                                     for(p=0; p<k; p++)
                                      y=max(y,a[i][p]);
                                      if(l==y)
                                       f=1;
                               }    
                         if(f==0)
                         break;
                    }
                      if(f==0)
                      break;
                    }
                    fout<<"Case #"<<q<<": ";
                    if(f==0)
                    fout<<"NO\n";
                    else
                    fout<<"YES\n";
                    q++;
      }
      fin.close();
      fout.close();

system("pause");
}
