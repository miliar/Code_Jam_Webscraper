#include<iostream>
#include<fstream>
using namespace std;
void finddigits(int x[10], int n)
{
    while(n)
    {
        x[n%10]=1;
        n=n/10;
    }
}
int main()
{
    int t,s,i,j,k;
    long long n;
    int x[10];
    ifstream in;
    ofstream out;
    in.open("INPUT.in");
    out.open("OUTPUT.txt");
    in>>t;
    for(i=1;i<=t;i++)
    {
        in>>n;
        if(n==0)
        {
            out<<"Case #"<<i<<": INSOMNIA"<<"\n";
        }
        else
        {
            j=1;
            while(1)
            {
                finddigits(x,n*j);
                s=0;
                for(k=0;k<=9;k++)
                {
                    if(x[k]==1)
                        s++;
                }
                if(s==10)
                {
                    out<<"Case #"<<i<<": "<<n*j<<"\n";
                    for(k=0;k<=10;k++)
                        x[k]=0;
                    break;
                }
                j++;
            }

        }
        }
}
