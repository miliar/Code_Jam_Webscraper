#include<fstream>
#include<iostream>
using namespace std;
long minima(long p, long q)
{
    if(p<q)
        return p;
    else
        return q;
}
long hcf(long p, long q)
{
    long hcf = 1;
    for(int i=1;i<=minima(p, q);i++)
        if(p%i==0 && q%i==0)
            hcf = i;
    return hcf;
}
int main()
{
    int t, j;
    long p=0, q=0, fac=0;
    char inp[100];
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt1.in");
    fout.open("output.out");
    fin>>t;
    for(int i=0;i<t;i++)
    {
        fin>>inp;
        j=0;
        p=0;
        q=0;
        for(;inp[j]!='/';j++)
        {
            p*=10;
            p+=(long)(inp[j]-48);
        }
        j++;
        for(;inp[j];j++)
        {
            q*=10;
            q+=(long)(inp[j]-48);
        }
        fac = hcf(p, q);
        p/=fac;
        q/=fac;
        if(i==1)
            cout<<p<<endl<<q;
        long check = q;
        while(check>1)
        {
            if(check%2!=0)
            {
                fout<<"Case #"<<i+1<<": impossible"<<endl;
                    break;
            }
            check/=2;
        }
        if(check!=1)
            continue;
        double num = (double)((double)q/(double)p);
        double samp = 2;
        for(int k=1;;k++)
        {
            if(num<=samp)
            {
                fout<<"Case #"<<i+1<<": "<<k<<endl;
                break;
            }
            samp*=2;
        }
    }
}
