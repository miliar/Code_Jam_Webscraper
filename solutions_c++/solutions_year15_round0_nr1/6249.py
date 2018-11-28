#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    long i,t;
    ifstream f1;
    f1.open("IN.txt");
    ofstream f2;
    f2.open("OP.txt");
    f1>>t;
    for(i=1;i<=t;i++)
    {
        long j,s,x,ans=0;
        f1>>s;
        string A;
        f1>>A;
        x=A[0]-48;
        for(j=1;j<s+1;j++)
        {
            long a=0;
            if(j>x)
                {
                   a= j-x;
                   ans+=a;
                }
            x=x+A[j]-48+a;
        }
        f2<<"Case #"<<i<<": "<<ans<<"\n";
    }
    f1.close();
    f2.close();
    return 0;
}
