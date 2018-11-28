#include <bits/stdc++.h>
using namespace std;

int t;

int n;

int p, r, s;

string wyg[17][3];

int licz[17][3][3];

int porz[1007];

string wyn;

int main()
{
    porz['P']=0;
    porz['R']=1;
    porz['S']=2;
    wyg[0][0]="P";
    wyg[0][1]="R";
    wyg[0][2]="S";
    for (int i=1; i<=12; i++)
    {
        for (int j=0; j<3; j++)
        {
            int l=(j+1)%3;
            wyg[i][j]=min(wyg[i-1][j], wyg[i-1][l])+max(wyg[i-1][j], wyg[i-1][l]);
            for (int k=0; k<(1<<i); k++)
            {
                licz[i][j][porz[wyg[i][j][k]]]++;
            }
        }
    }
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        int czy=0;
        wyn="Z";
        for (int i=0; i<3; i++)
        {
            if (licz[n][i][0]==p && licz[n][i][1]==r && licz[n][i][2]==s)
            {
                czy=1;
                wyn=min(wyn, wyg[n][i]);
            }
        }
        if (czy)
        cout << "Case #" << tt << ": " << wyn << endl;
        else
        cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
