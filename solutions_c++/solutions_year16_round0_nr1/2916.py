#include <fstream>
using namespace std;
int main()
{
    int t, n, ans, count, i, N, c, m, temp;

    ofstream op;
    op.open("output.in");

    ifstream ip;
    ip.open("A-large.in");

    ip>>t;
    for(c=1;c<=t;c++)
    {
        ip>>n;
        if(n==0)
            op<<"Case #"<<c<<": INSOMNIA\n";
        else
        {
            int a[10]={0};
            count=0;
            for(i=1;;i++)
            {
                N=n*i;
                m=N;
                while(m)
                {
                    temp=m%10;
                    if(a[temp]==0)
                    {
                        a[temp]=1;
                        count++;
                    }
                    m=m/10;
                }
                if(count==10)
                {
                    op<<"Case #"<<c<<": "<<N<<endl;
                    break;
                }
            }
        }
    }
    ip.close();
    op.close();
    return 0;
}
