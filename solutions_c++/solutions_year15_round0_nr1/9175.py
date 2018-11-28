#include <fstream>
#include<cstring>
using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

int t,lenght,n,k,nr,i,suma,sol;
char c;
char s[1020];

int main()
{
    fin>>t;
    for(k=1;k<=t;++k)
    {
        sol=0;
        suma=0;
        fin>>n;
       // fin>>c;
       fin.get();
        fin.get(s,n+10);
        lenght=strlen(s);
        for(i=0;i<lenght;++i)
        {
            if(s[i]==0) continue;
            nr=s[i]-'0';
            if(suma>=i)
                suma+=nr;
            else
            {
                sol+=i-suma;
                suma=i+nr;
            }
        }
        fout<<"Case #"<<k<<": "<<sol<<'\n';
    }

    return 0;
}
