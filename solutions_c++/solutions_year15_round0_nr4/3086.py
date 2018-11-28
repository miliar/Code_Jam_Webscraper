#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
    long int t,i,x,r,c;
    ifstream f1;
    ofstream f2;
    f1.open("IN.txt");
    f2.open("OP.txt");
    f1>>t;
    for(i=1;i<=t;i++)
    {
        f1>>x>>r>>c;
        long a;
        a=x/2;
        if((x==2 && (r*c)%2==0)|| x==1)
            f2<<"Case #"<<i<<": "<<"GABRIEL\n";
        else if(r>a && c>a && (((r*c)%x)==0))
                f2<<"Case #"<<i<<": "<<"GABRIEL\n";
        else
            f2<<"Case #"<<i<<": "<<"RICHARD\n";
    }
    f2.close();
    f1.close();
    return 0;
}
