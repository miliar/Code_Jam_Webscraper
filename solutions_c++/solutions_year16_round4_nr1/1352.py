#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

string Mikell(char c)
{
    if (c=='R'){return "RS";}
    if (c=='S'){return "PS";}
    if (c=='P'){return "PR";}
    return "exit";
}

void kifejt(vector<string>& Verseny, int N)
{
    for (int i=0; i<N;i++)
    {
        string s;
        for (int k=0; k<Verseny[i].length(); k++)
        {
            s+=Mikell(Verseny[i][k]);
        }

        Verseny.push_back(s);
    }
}

bool stat(string V, int R, int P, int S)
{
    int r=0;
    int p=0;
    int s=0;
    for (int i=0; i<V.length(); i++)
    {
        if (V[i]=='R'){r++;}
        if (V[i]=='S'){s++;}
        if (V[i]=='P'){p++;}
    }
    return (s==S) && (p==P) && (R==r);
}

string rendez(string s, int N)
{
    int szorzo=2;
    for (int i=1; i<N; i++)
    {
        string news;
        for (int j=0; j<s.length(); j+=2*szorzo)
        {
            string s1=s.substr(j,szorzo);
            string s2=s.substr(j+szorzo, szorzo);
            cout<<s1<<" "<<s2<<" "<<i<<endl;
            if (s1.compare(s2)>0)
            {
                news+=s2;
                news+=s1;
            }else
            {
                news+=s1;
                news+=s2;
            }

        }
        szorzo*=2;
        s=news;
    }
    return s;

}

int main()
{
    ifstream f("A-large.in");
    ofstream fki("mo.txt");
    int t;
    f>>t;
    for (int i=1; i<=t; i++)
    {
        int N,R,P,S;
        f>>N>>R>>P>>S;
        vector <string> Verseny1;
        vector <string> Verseny2;
        vector <string> Verseny3;
        string sol="IMPOSSIBLE";
        Verseny1.push_back("P");
        Verseny2.push_back("R");
        Verseny3.push_back("S");
        kifejt(Verseny1, N);
        kifejt(Verseny2, N);
        kifejt(Verseny3, N);
        if (stat(Verseny1[N],R,P,S)){sol=Verseny1[N];}
        if (stat(Verseny2[N],R,P,S)){sol=Verseny2[N];}
        if (stat(Verseny3[N],R,P,S)){sol=Verseny3[N];}
        if (sol.compare("IMPOSSIBLE")!=0){sol=rendez(sol,N);}
        fki<<"Case #"<<i<<": "<<sol<<endl;
    }
    f.close();
    fki.close();
    return 0;
}
