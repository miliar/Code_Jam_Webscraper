#include<bits/stdc++.h>
using namespace std;
#define MAX 1000001
typedef long long ll;

int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t; IF >> t;
    for(int tt=1;tt<=t;tt++)
    {
        string s; IF >> s;
        int a[26]={0};
        for(int i=0;i<s.size();i++)
            a[s[i]-'A']++;
        int c[10]={0};

        c[0]=a['Z'-'A'];
        a['E'-'A'] -= c[0]; a['R'-'A'] -= c[0]; a['O'-'A'] -= c[0];

        c[6]=a['X'-'A'];
        a['I'-'A'] -= c[6]; a['S'-'A'] -= c[6];

        c[2]=a['W'-'A'];
        a['T'-'A'] -= c[2]; a['O'-'A'] -= c[2];

        c[8]=a['G'-'A'];
        a['E'-'A'] -= c[8];a['I'-'A'] -= c[8];a['H'-'A'] -= c[8];a['T'-'A'] -= c[8];

        c[3]=a['H'-'A'];
        a['T'-'A'] -= c[3];a['R'-'A'] -= c[3];a['E'-'A'] -= c[3];a['E'-'A'] -= c[3];

        c[4]=a['U'-'A'];
        a['F'-'A'] -= c[4];a['O'-'A'] -= c[4];a['R'-'A'] -= c[4];

        c[5]=a['F'-'A'];
        a['I'-'A'] -= c[5];a['V'-'A'] -= c[5];a['E'-'A'] -= c[5];

        c[7]=a['V'-'A'];
        a['S'-'A'] -= c[7];a['E'-'A'] -= c[7];a['E'-'A'] -= c[7];a['N'-'A'] -= c[7];

        c[1]=a['O'-'A'];
        a['E'-'A'] -= c[1];a['N'-'A'] -= c[1];

        c[9]=a['E'-'A'];
        a['N'-'A'] -= c[9];a['I'-'A'] -= c[8];a['N'-'A'] -= c[9];

        if(0)
        {
            for(int i=0;i<10;i++)
                OF << c[i] << " ";
            OF << endl;
        }
        OF << "Case #" << tt << ": ";
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<c[i];j++)
                OF << i;
        }
        OF << endl;
    }
    OF.close(); IF.close();
}


