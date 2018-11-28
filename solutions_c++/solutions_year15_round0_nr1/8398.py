#include<fstream>
#include<conio.h>
using namespace std;
ifstream in("p.in");
ofstream out("p.out");
int main()
{
    int t,i,j,smax,s=0,r=0;
    char sir[1001];
    in>>t;
    for(i=1;i<=t;i++)
    {
        in>>smax;
        for(j=0;j<=smax;j++)
        {
            in>>sir[j];
            if(s>=j) s+=sir[j]-'0';
            else
            {
                r+=j-s;
                s=j+sir[j]-'0';
            }
        }
        out<<"Case #"<<i<<": "<<r<<"\n";
        r=0;
        s=0;
    }
    return 0;
}
