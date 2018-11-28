#include <fstream>

using namespace std;
int n, mx, a, v[100000], t, nrmx, nrmut, M;
bool ok;
int main()
{
    ifstream f("pan.in");
    ofstream g("pan.out");
    f>>t;
    for (int i=1; i<=t; i++)
    {
        f>>n;
        mx=0;
        nrmx=1;
        for (int j=1; j<=n; j++)
        {
            f>>v[j];
            if (v[j]>mx) mx=v[j];
        }
        M=mx;
        /*nrmax==maximul local*/
        while (nrmx<mx)
        {
            nrmut=0;
            for (int j=1; j<=n; j++)
                if (v[j]>nrmx)
                {
                    if (v[j]%nrmx==0) nrmut=nrmut+v[j]/nrmx-1;
                                 else nrmut=nrmut+v[j]/nrmx;
                }
            a=nrmut+nrmx;
            if (a<M) M=a;
            nrmx++;
        }
        g<<"Case #"<<i<<": "<<M<<'\n';
    }
    return 0;
}
