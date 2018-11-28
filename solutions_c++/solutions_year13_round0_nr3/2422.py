#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
bool palin(long long int n)
{
    long long int S[120],i,j,l;
    l=0;
    while(n)
    {
        S[++l]=n%10;
        n=n/10;
    }
    for(i=1,j=l;i<=l/2;i++,j--)
    {
        if(S[i]!=S[j])
        return false;
    }
    return true;
}
int A[4000004],B[4000004];
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    double d,e;
    long long int i,j,k,l,m,n,t,count,T;

    bool f;

    for(i=1;i<=4000000;i++)
    {
        A[i]=0;
    }

    for(i=1;i<=4000000;i++)
    {
        if(palin(i))
        if(palin(i*i))
        A[i]++;
    }

    B[0]=0;
    for(i=1;i<=4000000;i++)
    {
        B[i]=B[i-1]+A[i];
    }

    fin>>t;
    T=t;
    while(t--)
    {
        fin>>i>>j;
        e=j;
        d=sqrt(e);
        j=d;

        e=i;
        d=sqrt(e);
        k=d;

        if(k*k==i)
        i=k;
        else
        i=k+1;

        if(i>4000000)
        {
            fout<<"Case #"<<T-t<<": "<<"0"<<"\n";
        }
        else
        {
            if(j>4000000)
            j=4000000;

            count=B[j]-B[i]+A[i];
            fout<<"Case #"<<T-t<<": "<<count<<"\n";
        }
    }
    return 0;
}
