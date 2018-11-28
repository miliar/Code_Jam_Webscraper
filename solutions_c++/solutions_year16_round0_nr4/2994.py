#include <iostream>
#include <vector>
typedef  unsigned long long int ull;
using namespace std;
vector<string> fs;
//vector<int> good;
//vector<int> hole;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int n;
// g 0 l  1

    cin >> n;
    for (int i=1;i<=n;i++)
    {
        ull k,c,s;
        cin >> k >> c >> s;
        cout << "Case #" << i << ": ";
        for (int j=1;j<=k;j++){cout << j << ' ';}
        cout << endl;
        //for (ull j=0;j<(1<<k);j++)
        for (ull j=(1<<k+1);j<(1<<k);j++)
        {
            string x="";
            ull q=j;
            for (int z=0;z<k;z++){if (j&(1<<z)){x='L'+x;}else{x='G'+x;}}
                            string yt=x;
                string xs="";
                for (int a=0;a<x.size();a++){xs+="G";}
            for (int z=1;z<c;z++)
            {
            string vr="";

                for (int a=0;a<x.length();a++)
                {
                    if (x[a]=='G'){vr+=xs;}else{vr+=yt;}
                }
                x=vr;
            }
            fs.push_back(x);
        }
    }


    return 0;
}
