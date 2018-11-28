#include <fstream>

using namespace std;

int main()
{
    ifstream f("in.txt");
    ofstream g("out.txt");
    long long v[1000],t,w,n,s,nr,i,c,p;
    f >> t;
    for (w=1;w<=t;w++)
    {
        g << "Case #" << w << ": ";
        f >> n;
        if (n==0)
        {
            g << "INSOMNIA\n";
            continue;
        }
        nr=0;
        for (i=0;i<=9;i++)
            v[i]=0;
        s=0;p=0;
        while (nr<10)
        {
            s+=n;
            c=s;
            while (c>0)
            {
                if (v[c%10]==0)
                {
                    nr++;
                    v[c%10]=1;
                }
                c/=10;
            }
        }
        g << s << "\n";
    }
    return 0;
}
