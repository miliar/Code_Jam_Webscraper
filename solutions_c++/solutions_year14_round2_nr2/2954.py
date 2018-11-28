#include<iostream>
#include<stdio.h>
#include<fstream>
#include<string.h>
using namespace std;
long long  A, B, K, S=0;

int solution()
{
    int i, j;
    long long c, S1=0;
    for(i=0; i<A; i++)
    {
        for(j=0; j<B; j++)
        {
            c=i&j;
            if(c<K)
                S1++;
        }
    }
    return S1;
}

int main()
{
    int n, m=1;
    ifstream fin("A-small-practice.in");
    ofstream fout("A-small-practice.out", ios::app);
    fin>>n;
    while(m<=n)
    {
        fin>>A>>B>>K;
        S=solution();
            fout<<"Case #"<<m<<": "<<S<<endl;
        m++;
    }
    fin.close();
    fout.close();
    return 0;
}

