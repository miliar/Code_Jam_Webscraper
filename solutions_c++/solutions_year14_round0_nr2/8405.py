//@author Zubaidullo Niimatullo uulu
#include <iostream>
#include <stdlib.h>
#include <iomanip.h>
#include <stdio.h>
#include <string>
#include <fstream>
using namespace std;
double check(double c, double f, double x) {
       double ans,sum=0,q=2,sum1=0,z=0;
       bool flag=false;
       ans=x/q;
       sum=c/q;
              while(flag!=true)
              {
              if (sum+(x/(q+f))<ans) ans=sum+(x/(q+f));
              else flag=true;
              q+=f;              
              sum+=c/q;
              }
       return ans;
       }
int main()
{
int t,l;
int i,j;
double c,f,x;
    ifstream fin("B-large.in");
    ofstream fout("output.txt");
    fin>>t; 
    for (l=0; l<t; l++)
    {
    fin>>c>>f>>x;
    fout<<"Case #"<<l+1<<": ";
    fout<<fixed<<setprecision(7)<<check(c,f,x)<<endl;                 
    } 
return 0;
}
