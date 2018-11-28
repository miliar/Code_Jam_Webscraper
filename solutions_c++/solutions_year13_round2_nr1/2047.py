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
{     unsigned long long int i,j,k,l,n,m,p,t,q,f,y,o;
       ifstream fin;
       ofstream fout;
      fin.open("Input.txt");
      fout.open("Output.txt");
      fin>>n;
     // cout<<n;
      q=1;
      while(q<=n)
      {
                 fin>>m>>k;
                unsigned long long  int a[k];
                 
                  for(j=0; j<k; j++)//{
                   fin>>a[j];
                   //cout<<a[i][j];}
                   sort(a,a+k);
                  // for(i=0; i<k; i++)
                  // cout<<a[i];
                   l=0;
                   for(i=0; i<k; i++)
                     {
                      if(a[i]<m)
                      m+=a[i];
                      else if(m<=a[i])
                      {                          
                                                  p=0;
                                                  o=0;
                                                  
                                                  while(m<=a[i]&&m+m-1!=o)
                                                  {
                                                    m+=m-1;
                                                    o=m;
                                                    p++;
                                                    //cout<<m;
                                                  }
                                                  //cout<<p;
                                                  if(m>a[i])
                                                  m+=a[i];
                                                  if(p+l>=k||p>=k-i)
                                                  {
                                                  p=k-i;
                                                  l+=p;
                                                  if(l>k)
                                                  l=k;
                                                  break;
                                                  }
                                                  //else if(p)
                                                  l+=p;
                           
                      }
                      
                     }
                      
                     //cout<<l<<"\n";
                    fout<<"Case #"<<q<<": ";
                    fout<<l<<"\n";
                    
                    q++;
                    
      }
      fin.close();
      fout.close();

//system("pause");
}
