#include<iostream>
#include<stdlib.h>
#include <string>
#include<math.h>
#include <cstdlib>
#include <cstring>  
#include <sstream>
#include <algorithm>
using namespace std;
main(void)
{
          int i = 0,x,y,c,h=0,r1,a,b,aux,k;
          float r,r2;
          freopen("C-small-attempt1.in","rt",stdin);
          freopen("C-small-attempt1.out","wt",stdout);
          cin>>c;
          int v[c];
          getchar();
          while(i != c)
          {
                  h=0;
                  cin>>x>>y;
                  for(int j = x;j <= y;j++)
                  {
                          if(j < 10)
                          {
                               r = pow(j,0.5);
                               r1 = (int)pow(j,0.5);
                               r2 = r1 - r;
                               if(r2 == 0)
                               {
                                    h++;
                               }
                          }
                          else
                          {
                              a = j;
                              aux = 0;
                              while(a > 10)
                              {
                                      b = a%10;
                                      a = a / 10;
                                      aux = (aux + b)*10;
                              }
                              aux = aux + a;
                              if(j == aux && j != y + 1)
                              {
                                   r = pow(j,0.5);
                                   r1 = (int)pow(j,0.5);
                                   r2 = r1 - r;
                                   if(r2 == 0)
                                   {
                                         h++;
                                   }
                              }
                          }
                  }
                  v[i] = h;
                  i++;
          }
          k = 1;
          for(i = 0;i < c; i++)
          {  
                cout<<"Case #"<<k;
                cout<<": "<<v[i]<<"\n";
                k++;
          }
}

