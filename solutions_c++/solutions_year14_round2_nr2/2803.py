#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int solve(int a,int b,int k)
{
    int i,j,ctr;
    ctr=0;
    for(i=0;i<a;i++)
    {
        for(j=0;j<b;j++)
        {
            if((i&j)<k)
            {
                ctr++;
            }
        }
    }
    return ctr;
}
int main()
{
   ifstream fin;    //B-small-attempt0.in
   fin.open("B-small-attempt1.in",ios::in);
   ofstream fout;
    fout.open("B-small-attempt1.out",ios::out);
   int t,tc,a,b,k;
   fin>>tc;
   for(t=1;t<=tc;t++)
   {
       fin>>a>>b>>k;
       fout<<"Case #"<<t<<": "<<solve(a,b,k)<<"\n";
   }
    return 0;

}

