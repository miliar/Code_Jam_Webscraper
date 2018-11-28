#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    ifstream f1;
    FILE *f2;
    f1.open("B-large.in");
    f2=fopen("output.out","w");
    int t,it=1;
    double c,f,x,temp,z;
    //cout<<"\n chala \n";
    f1>>t;
    while(it<=t)
    {
               f1>>c>>f>>x;
               //cout<<"\n c = "<<c<<" , f , "<<f<<" x = "<<x<<endl;
               temp = x/2.0;
               if(x<=c)
               {
                       fprintf(f2,"Case #%d: %0.7f\n",it++,temp);
                       //cout<<"\n temp = "<<temp<<endl;
                       //f2<<temp<<setprecision(8)<<endl;
                       }
               else
               {
                   for(int i=1;i<x;i++)
                   {
                           //cout<<"\n no. of farms "<<i<<endl;
                           z = 0;
                              for(int j=0;j<i;j++)
                              {
                                      z += (c/(2.0+(j*f))); 
                                      //cout<<"\n z = "<<z<<" , at j = "<<j<<endl;
                                      }
                              z += (x/(2.0+(i*f)));
                              if(temp-z>0)temp = z;
                              else break;
                              }
                   fprintf(f2,"Case #%d: %0.7f\n",it++,temp);
                   //f2<<temp<<setprecision(8)<<endl;
                   }
    //cout<<"\n in while\n";
               }
    f1.close();
    fclose(f2);
    //system("pause");
    return 0;
    }
