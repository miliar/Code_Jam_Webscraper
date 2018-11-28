#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int fair(int a)
{
    int b,c=0,d=a,e=0;
    while(a!=0)
    {
        b=a%10;
        a=a/10;
        c=c*10+b;
    }
    if(d==c) e=1;
    return e;
}

int square(int a)
{
    int b,c=0;
    b=sqrt(a);
    if(b*b==a) c=1;
    return c;
}

int main()
{
    ifstream in("googlecodejam.in");
    ofstream out("googlecodejam.out");
    int t,a,b,c;
    in>>t;
    for(int i=0;i<t;i++)
    {
        in>>a;
        in>>b;
        c=0;
        for(int j=a;j<=b;j++)
        {
            if((fair(j)==1)&&(square(j)==1)&&(fair(sqrt(j))==1)) c++;
        }
        out<<"Case #"<<i+1<<": "<<c<<endl;
    }
    return 0;
}
