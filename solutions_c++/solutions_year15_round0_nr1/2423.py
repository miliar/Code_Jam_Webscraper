#include<fstream>
#include<string>

using namespace std;

int t,smax,suma,nr,prieteni;
string s;

ifstream f("A-large.in");
ofstream g("standing.out");

int main()
{
    f>>t;
    for(int i=1;i<=t;++i)
    {
        f>>smax>>s;
        g<<"Case #"<<i<<": ";
        suma=0;
        prieteni=0;
        for(int j=0;j<s.size();++j)
        {
            if(j>suma) prieteni+=j-suma, suma=j;
            nr=s[j]-'0';
            suma+=nr;
        }
        g<<prieteni<<'\n';
    }
}
