#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <sstream>
using namespace std;

bool good (long long cnt[10]) {
    for(int i=0; i<10;i++) {
        if(cnt[i]<1) return false;
    }

    return true;
}

void megold(istream& in, ostream &out)
{
    int n;
    in>>n;

    if(n==0) {
        out<<"INSOMNIA";
        return;
    }

    long long sum=0;
    long long cnt[10];
    for(int i=0; i<10;i++) {
        cnt[i]=0;
    }

    while(!good(cnt)) {
        sum+=n;
        long long l=sum;
        while(l>0) {
            cnt[l%10]=1;
            l=l/10;
        }
    }

    out<<sum;
}

int main()
{
    ifstream in("A-large.in");
    ofstream out("sheep.out");
    int n;
    in>>n;

    //out<<setprecision(12);
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
