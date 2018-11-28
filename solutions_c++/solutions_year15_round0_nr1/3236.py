#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void megold(istream& in, ostream &out)
{
    int max;
    string str;
    in>>max>>str;
    int standing=0;
    int inv=0;
    for(int i=0; i<=max; i++)
    {
        int n=str[i]-'0';
        if(n==0) continue;

        if(standing<i) {
            int ninv=i-standing;
            inv+=ninv;
            standing+=ninv;
        }

        standing+=n;
    }

    out<<inv;
}

int main()
{
    ifstream in("A-large.in");
    ofstream out("primadonna.out");
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
