#include <iostream>
#include<fstream>
#include<cmath>

using namespace std;

int bleatrix(int n)
{
    if(n<=0)
        return 0;
    int afill=0,a[10]={0},i=1;
    while(afill<10)
    {
        int ni=n*i;
        while(ni)
        {
            int s=ni%10;
            if(a[s]==0)
            {
                afill++;
                a[s]=1;
            }
            ni/=10;
        }
        i++;
    }
    return n*(i-1);
}

int main()
{
    ifstream fin("input.in",ios::in);
    ofstream fout("output.txt",ios::out);
    int t,ti;
    fin>>t;
    ti=t;
    while(t--)
    {
        int n;
        fin>>n;
        if(n==0)
            fout<<"Case #"<<ti-t<<": INSOMNIA"<<endl;
        else
            fout<<"Case #"<<ti-t<<": "<<bleatrix(n)<<endl;
    }
    return 0;
}
