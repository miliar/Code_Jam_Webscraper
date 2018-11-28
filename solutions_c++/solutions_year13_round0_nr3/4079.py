#include <iostream>
#include <fstream>
#include <string>

//This program requires 64-bit integers.

using namespace std;

bool ispal(long long int n)
{
    long long int r=0,x=n;
    while(x>0){r=r*10+x%10; x/=10;}
    return (n==r);
}

int main(int args, char* arg[])
{
    if(args<2) return 1;
    ifstream fin(arg[1],ifstream::in);
    ofstream fou("Cout.txt",ofstream::out);

    int tc,t; fin>>t; fin.ignore(100,'\n');

    //precalc
    const long long int MAX=1e14;
    long long int a,b, k, fas[50]={0}; int i,j,c=0;
    for(k=1;k*k<MAX;k++)
    {
        if(ispal(k)&&ispal(k*k)) { fas[c++]=k*k; }
    }

    //test cases
    for(tc=1;tc<=t;tc++)
    {
        i=0; fin>>a>>b;
        while(i<c&&fas[i]<a) i++;
        j=i; while(j<c&&fas[j]<=b) j++;
        fou<<"Case #"<<tc<<": "<<(j-i)<<endl;
    }


    return 0;
}
