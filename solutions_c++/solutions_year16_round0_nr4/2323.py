#include <fstream>
#include <iostream>
using namespace std;
long long power(long long a, long long b)
{
    long long ans = 1;
    while(b > 0)
    {
        if(b%2 == 1)
            ans *= a;
        a *= a;
        b = b>>1;
    }
    return ans;
}
int main()
{
    long long t,Case,k,c,s,A,B,i;
    ifstream ip;
    ip.open("D-small-attempt1.in");
    ofstream op;
    op.open("output.in");
    ip>>t;
    for(Case=1;Case<=t;Case++)
    {
        ip>>k>>c>>s;
        op<<"Case #"<<Case<<": ";
        if(k==1)
        {
            op<<"1 \n";
            continue;
        }
        A = power(k,c);
        B = (A-1)/(k-1);
        for(i=0;i<A;i=i+B)
            op<<i+1<<" ";
        op<<endl;
    }
    ip.close();
    op.close();
    return 0;
}
