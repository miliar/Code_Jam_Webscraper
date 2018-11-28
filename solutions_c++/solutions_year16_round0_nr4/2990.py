#include<bits/stdc++.h>
using namespace std;
ifstream fin("D-small-attempt1.in");
ofstream fout("output4.txt");
long long fpow(long long x,long long n)
{
    if(n==0) return 1;
    long long temp;
    temp=fpow(x,n/2);
    if(n%2==0)
        return temp*temp;
    else
        return x*temp*temp;
}
int main()
{

    long long int t;
    fin>>t;long long int i=0;
    while(t--)
    {i++;
        long long int n,c,k;
        fin>>n>>c>>k;
        fout<<"Case #"<<i<<": ";
        for(long long int j=0;j<k;j++)
            fout<<(j*(fpow(n,c)/n))+1<<" ";
            fout<<"\n";
    }
}
