#include <bits/stdc++.h>
using namespace std;

int t;

int n, m;

vector <int> graf[107];
int oj[107];
char wcz[107];

char faj[10][27];
int roz[10];

int ile[10];
int d=10000;

string mam;
string rob;

int kmp[207];
int it;

int suma;

int kt(vector <string> &wek)
{
    suma=0;
    for (int i=0; i<wek.size(); i++)
    {
        suma+=wek[i].size();
    }
    suma=(rand()%suma)+1;
    for (int i=0; i<wek.size(); i++)
    {
        suma-=wek[i].size();
        if (suma<=0)
        {
            return i;
        }
    }
}

string losuj(int v)
{
    vector <string> wek;
    string ret="";
    for (int i=0; i<graf[v].size(); i++)
    {
        wek.push_back(losuj(graf[v][i]));
    }
    while(!wek.empty())
    {
        for (int i=0; i<wek.size(); i++)
        {
            if (wek[i]=="")
            {
                swap(wek[i], wek.back());
                wek.pop_back();
                i--;
            }
        }
        if (wek.empty())
        continue;
        int x=kt(wek);
        ret+=wek[x][wek[x].size()-1];
        wek[x]=wek[x].substr(0, wek[x].size()-1);
    }
    ret+=wcz[v];
    reverse(ret.begin(), ret.end());
    return ret;
}

int czyma(int v)
{
    for (int i=0; i<=rob.size()+2; i++)
    {
        kmp[i]=0;
    }
    for (int i=2; i<rob.size(); i++)
    {
        it=kmp[i-1];
        while(it && rob[i]!=rob[it+1])
        it=kmp[it];
        if (rob[i]==rob[it+1])
        kmp[i]=it+1;
        if (kmp[i]==v)
        return 1;
    }
    return 0;
}

int main()
{
    srand(time(0));
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        cerr << tt << endl;
        printf("Case #%d: ", tt);
        scanf("%d", &n);
        for (int i=0; i<=n; i++)
        {
            graf[i].clear();
        }
        for (int i=1; i<=n; i++)
        {
            scanf("%d", &oj[i]);
            graf[oj[i]].push_back(i);
        }
        scanf("%s", wcz+1);
        wcz[0]='#';
        scanf("%d", &m);
        for (int i=1; i<=m; i++)
        {
            scanf("%s", faj[i]+1);
            roz[i]=0;
            for (int j=1; faj[i][j]; j++)
            roz[i]++;
            ile[i]=0;
        }
        for (int i=1; i<=d; i++)
        {
            mam=losuj(0);
            for (int j=1; j<=m; j++)
            {
                rob="$";
                for (int l=1; l<=roz[j]; l++)
                {
                    rob+=faj[j][l];
                }
                rob+=mam;
                ile[j]+=czyma(roz[j]);
            }
        }
        for (int i=1; i<=m; i++)
        {
            printf("%.9lf ", (double)ile[i]/d);
        }
        printf("\n");
    }
    return 0;
}
