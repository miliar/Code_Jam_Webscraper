#include <fstream>
#include <string>
using namespace std;
int t, nr=0, smx, stand;
string s;
bool ok;
int main()
{
    ifstream f("shy.in");
    ofstream g("shy.out");
    f>>t;
    for (int i=1; i<=t; i++)
    {
        nr=0;stand=0;
        f>>smx;
        f>>s;
        for (int j=0; j<s.size(); j++)
        {
            ok=0;
            while (ok!=1)
            {
                if (stand<j) {nr++;stand=stand+1;}
                    else ok=1;
            }
            stand=stand+s[j]-'0';
        }
        //g<<stand<<" ";
        g<<"Case #"<<i<<": "<<nr<<'\n';
    }
    return 0;
}
