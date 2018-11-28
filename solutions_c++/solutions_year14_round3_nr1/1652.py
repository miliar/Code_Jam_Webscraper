#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;

long long  gcd(long long a, long long b) {
    while (b != 0) {
        long long  m = a % b;
        a = b;
        b = m;
    }
    return a;
}

void megold(istream& in, ostream &out)
{
    long long p, q;
    string s;
    in>>s;
    int pos=s.find("/");
    p=strtod(s.substr(0,pos).c_str(), NULL);
    q=strtod(s.substr(pos+1).c_str(), NULL);


    long long k=gcd(p, q);
    p/=k;
    q/=k;
    //cout<<p<<' '<<q<<endl;

//cout<<"y"<<endl;


    int nq=q;
    while(nq>1) {
        if(nq%2==1) {
            out<<"impossible";
            return;
        } else {
            nq=nq/2;
        }
    }
//cout<<"z"<<endl;

    //if(p>=q) { out<<0; return; }

    int ret=0;
    while(p<q) {
        ret++;
        q=q/2;
    }

    if(ret>40) {
        out<<"impossible";
        return;
    }

    out<<ret;
}

int main()
{
    ifstream in("A-small-attempt1.in");
    //ifstream in("test.in");
    ofstream out("cons.out");
    int n;
    in>>n;

    for(int i=1; i<=n; i++)
    {
        out<<"Case #"<<i<<": ";
        megold(in, out);
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
