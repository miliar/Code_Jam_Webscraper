#include<iostream>
#include<fstream>
#include<string>
using namespace std;

string s;
fstream wejscie, wyjscie;

int main()
{
    wejscie.open("A-large.in", ios::in);
    wyjscie.open("wyjscie.txt", ios::out);
    int t;
    wejscie>>t;
    for(int i=1; i<=t; i++)
    {
        int m, wynik=0, klaszcz=0;
        wejscie>>m>>s;
        for(int j=0; j<=m; j++)
        {
            if(s[j]=='0') continue;
            if(klaszcz>=j) klaszcz+=s[j]-48;
            else
            {
                wynik+=j-klaszcz;
                klaszcz=j+s[j]-48;
            }
        }
        wyjscie<<"Case #"<<i<<": "<<wynik<<"\n";
    }
}
