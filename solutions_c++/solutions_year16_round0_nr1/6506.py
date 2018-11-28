#include <bits/stdc++.h>

using namespace std;

int main()
{
    /*ofstream ini;
    ini.open("input.txt");
    ini<<"1000001\n";
    for(long int i=0;i<1000001;i++)
        ini<<i<<endl;
    ini.close();*/
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    int t,d;
    long int n,x,c;
    in>>t;
    for(int j=1;j<=t;j++)
    {
        out<<"Case #"<<j<<": ";
        in>>n;
        if(n==0)
        {
            out<<"INSOMNIA\n";
            continue;
        }
        x=1;
        bitset<10> a;
        while(1)
        {
            c=n*x;
            while(c!=0)
            {
                d=c%10;
                a.set(d);
                if(a.count()==10)
                    break;
                c/=10;
            }
            if(a.count()==10)
            {
                out<<n*x<<endl;
                break;
            }
            x++;
        }
    }
    return 0;
}
