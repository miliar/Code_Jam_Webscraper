#include<bits/stdc++.h>
using namespace std;
ifstream fin("D-small-attempt1.in");
ofstream fout("output6.txt");
long long fastpow(long long a,long long b)
{
    if(b==0) return 1;
    long long temp;
    temp=fastpow(a,b/2);
    if(b%2==0)
        return temp*temp;
    else
        return a*temp*temp;
}
int main()
{
    long long int t;
    fin>>t;long long int i=0;
    while(t--)
    {i++;
        long long int s,c,k;
        fin>>k>>c>>s;
        fout<<"Case #"<<i<<": ";
        for(long long int l=0;l<s;l++)
            fout<<(l*(fastpow(k,c)/k))+1<<" ";
            fout<<"\n";
    }
}
