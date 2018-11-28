#include <iostream>
#include <fstream>
using namespace std;
ifstream f("date.in");
ofstream g("date.out");
int t,ma,sum,sol,j,i;
char s[1004];
int main()
{
    f>>t;
    for(i=1;i<=t;i++)
    {
        f>>ma;
        f>>s;
        for(j=0;j<ma;j++)
        {
            sum+=(s[j]-'0');
            if (sum<j+1) sol++,sum++;
        }
        g<<"Case #"<<i<<": "<<sol<<"\n";
        sol=sum=0;
    }

    return 0;
}
