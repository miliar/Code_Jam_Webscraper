#include <iostream>
#include <fstream>
#define MAXC 256
#define MAXN 10

using namespace std;

int v[MAXC],T,d[MAXN];

int main()
{
    ifstream in("A-large.in");
    ofstream out("output.txt");
    in>>T;
    for(int k=1;k<=T;k++)
    {
        string s;
        in>>s;
        out<<"Case #"<<k<<": ";
        for(int i=0;i<s.size();i++)
            v[s[i]]++;
        while(v['Z']>0){v['Z']--;v['E']--;v['R']--;v['O']--;d[0]++;}
        while(v['W']>0){v['T']--;v['W']--;v['O']--;d[2]++;}
        while(v['U']>0){v['F']--;v['O']--;v['U']--;v['R']--;d[4]++;}
        while(v['F']>0){v['F']--;v['I']--;v['V']--;v['E']--;d[5]++;}
        while(v['X']>0){v['S']--;v['I']--;v['X']--;d[6]++;}
        while(v['V']>0){v['S']--;v['E']--;v['V']--;v['E']--;v['N']--;d[7]++;}
        while(v['O']>0){v['O']--;v['N']--;v['E']--;d[1]++;}
        while(v['N']>0){v['N']--;v['I']--;v['N']--;v['E']--;d[9]++;}
        while(v['G']>0){v['E']--;v['I']--;v['G']--;v['H']--;v['T']--;d[8]++;}
        while(v['T']>0){v['T']--;v['H']--;v['R']--;v['E']--;v['E']--;d[3]++;}
        for(int i=0;i<MAXN;i++)
            while(d[i]>0)
            {
                out<<i;
                d[i]--;
            }
        out<<endl;
    }
}
