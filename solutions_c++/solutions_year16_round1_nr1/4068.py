#include <fstream>
#include <string.h>
using namespace std;
int main()
{
    int t, l, ans, count, i, N, c, m;
    string a, temp;

    ofstream op;
    op.open("output.in");

    ifstream ip;
    ip.open("A-large.in");

    ip>>t;
    for(c=1;c<=t;c++)
    {
        ip>>a;
        l = a.size();
        temp=a[0];
        for(i=1;i<l;i++)
        {
            if((int)(a[i]-48)>=(int)(temp[0]-48))
                temp=a[i]+temp;
            else
                temp=temp+a[i];
        }
        op<<"Case #"<<c<<": "<<temp<<"\n";
    }
    ip.close();
    op.close();
    return 0;
}
