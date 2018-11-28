#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;
bool a[10];
bool ok ()
{
    for(int i=0;i<10;i++)if(!a[i]){return 0;}
     return 1;
}
int main()
{
    int t;
    int n;
    ifstream in("in.in");
    ofstream out("out.txt");
    in>>t;
    for(int q=1;q<=t;q++){

            in>>n;
    if(n==0){out<<"Case #"<<q<<": "<<"INSOMNIA"<<endl;continue;}
    int m=0;
    memset(a,0,sizeof(a));
    while(!ok()){
    m++;
    long long var=n*m;

    while(var)
    {
        if(!a[var%10]){a[var%10]=1;}
        var/=10;
    }

    }
    out<<"Case #"<<q<<": "<<n*m<<endl;

    }
    return 0;
}
