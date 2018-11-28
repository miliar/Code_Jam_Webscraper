#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <map>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
long long int prime(long long int n)
{
    if(n%2==0)return 2LL;
    for(long long int i=3;i<sqrt(n);i+=2)
        if(n%i==0)return i;
    return 0;
}
long long int cBase(long long int n,int base)
{
    if(n==0)return 0LL;
    return cBase(n/base,base)*10+n%base;
}
long long int tBase(long long int n,int base)
{
    if(n==0)return 0LL;
    return tBase(n/10,base)*base+n%10;
}
int main()
{
    ifstream fin;
    fin.open("C-small-attempt1.in");
    ofstream fout;
    fout.open("JAM.txt");
    int T;
    fin>>T;
    long long int divs[11]={0};
    for(int t=1;t<=T;t++)
    {
        int N,J;
        fin>>N>>J;
        N-=2;
        fout<<"Case #"<<t<<":"<<endl;
        for(long long int n=(1<<N),c=0;(n<=(1<<(N+1))-1) && (c<J);n++)
        {
            long long int number=n*2+1;
            number=cBase(number,2);
            for(int k=2;k<=10;k++){
                divs[k]=prime(tBase(number,k));
            }
            bool flag=true;
            for(int k=2;k<=10;k++)
                if(divs[k]==0)flag=false;
            if(flag)
            {
               fout<<number<<" ";
               for(int k=2;k<=10;k++)fout<<divs[k]<<" ";
               fout<<endl;
               c++;
            }
        }
    }
}
