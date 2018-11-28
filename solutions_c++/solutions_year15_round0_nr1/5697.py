#include <fstream>
using namespace std;
ifstream f("input.txt");
ofstream g("output.txt");
char s[1002];
int main()
{int t;
f>>t;
for(int i=1;i<=t;i++)
{
    int x;
    f>>x;
    f>>s;
    long long k=0,nr=0;
    for(int j=0;j<=x;j++)
        {if (k>=j)
            k+=s[j]-48;
        else
            if(s[j]!='0')
                nr+=j-k,k=j+s[j]-48;
        }
    g<<"Case #"<<i<<": "<<nr<<'\n';
}
return 0;
}
