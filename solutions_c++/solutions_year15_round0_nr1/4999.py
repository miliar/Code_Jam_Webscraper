#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T,t,s[1002],k,sum,nr;
    char c;

    ifstream f("shiness.in");
    ofstream g("shiness.out");

    f>>T;
    for (int i=1;i<=T;i++) {
            f>>t;
            k=0; nr=0;
            for (int j=0;j<=t+1;j++) {
                f.get(c);
                if (c>='0' && c<='9') s[k++]= c - '0';
            }
            sum=s[0];
            if (sum<1) { nr++; sum=sum+1; }
            for (int j=1;j<k-1;j++) {
                    sum=sum+s[j];
                    if (sum < j+1) { nr=nr+(j+1-sum); sum=sum+(j+1-sum); }
            }
            g<<"Case #"<<i<<": "<<nr<<'\n';
    }
    return 0;
}
