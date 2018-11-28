#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<fstream>
using namespace std;
int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("B-small-attempt0.in");
    f2.open("output.out");
    int t,a,b,k,count,c=1;
    f1>>t;
    while(c<=t)
    {
              count = 0;
              f1>>a>>b>>k;
              for(int i=0;i<a;i++)
              {
                      for(int j=0;j<b;j++)
                      {
                              if((i&j)<k)count++;
                              }
                      }
              f2<<"Case #"<<c++<<": "<<count<<endl;
              }
    //system("pause");
    return 0;
    }
