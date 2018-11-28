#include <fstream>
#include <iostream>
#include <string>

using namespace std;

ifstream in ("test.in");
ofstream ou ("test.out");

string a;

int main()
{
    long long t,i,j,ok,st,nr=0;
    in>>t;
    for (i=1;i<=t+1;++i){
        a.clear();
        getline(in,a);
        if (i==1)
            continue;
        ok=0;
        nr=0;
        for (j=0;j<a.length();++j){
            if (a[j]=='-' && !ok){
                st=j;
                ok=1;
            }
            if (a[j]=='+' && ok){
                ok=0;
                if (st==0)
                    nr++;
                else
                    nr+=2;
            }
        }
        if (ok){
            if (st==0)
                nr++;
            else
                nr+=2;
        }
        ou<<"Case #"<<i-1<<": "<<nr<<"\n";
    }
    ou.close();
    return 0;
}
