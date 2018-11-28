#include <fstream>
#include <cmath>
using namespace std;

int pal(long long x) {
    long long c,p;
    p=0;
    c=x;
    while (c) {
        p=p*10+c%10;
        c/=10;
    }
    if (p==x)
        return 1;
    return 0;

}
int nr;
int main() {
    int t,l,i;
    long long a,b;
    ifstream in("input.in");
    ofstream out("output.out");
    in>>t;
    for (l=1; l<=t; l++) {
        in>>a>>b;
        nr=0;
        for (i=sqrt(a); i<=sqrt(b)+1; i++)
            if (pal(i)&&pal(i*i)&&i*i>=a&&i*i<=b)
                nr++;
        out<<"Case #"<<l<<": "<<nr<<'\n';
    }
    out.close();
    return 0;
}
