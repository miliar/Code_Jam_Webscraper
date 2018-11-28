#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    int n,a;
    ifstream f("A-large.in");
    ofstream g("date.out");
    f>>n;
    int k;
    int suma;
    int rasp;
    string s;
    for(int i=1;i<=n;i++)
    {
        suma=0;
        rasp=0;
        f>>k;
        f>>s;
        for(int j=0;j<=s.size()-1;j++)
        {
            if(j>suma&&s[j]!='0')
            {
                rasp=rasp+(j-suma);
                suma=suma+(j-suma);
            }
            suma=suma+(s[j]-'0');
        }
        g<<"Case #"<<i<<": "<<rasp<<"\n";
    }
}
