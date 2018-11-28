#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#define f cin
#define g cout
#define NM 210
#define WM 10000

using namespace std;

int T;
int N, W;
string S;
vector<string> V;
string aux;
map<string, int> mymap;

vector<int> words[NM];

void parse ()
{
    V.clear();

    aux = "";
    S += ' ';
    for (int i=0; i<S.size(); i++)
        if (S[i] != ' ')
            aux += S[i];
        else
        {
            if (aux.size() != 0)
                V.push_back(aux);
            aux = "";
        }
}

void Read ()
{
    f >> N;
    getline(f, S);

    W = 0;
    mymap.clear();
    for (int i=1; i<=N; i++)
    {
        getline(f, S);
        parse();

        words[i].clear();
        for (int j=0; j<V.size(); j++)
        {
            if (mymap.find(V[j])==mymap.end())
                mymap[V[j]] = ++W;

            words[i].push_back(mymap[V[j]]);
        }
    }
}

int lang1[WM], lang2[WM];

void Solve ()
{
    for (int i=0; i<WM; i++)
        lang1[i]=lang2[i]=0;

    for (int i=0; i<words[1].size(); i++)
        lang1[words[1][i]] = 1;

    for (int i=0; i<words[2].size(); i++)
        lang2[words[2][i]] = 1;

    int M = N-2;
    int ANS = W + 1000;
    int nowANS = 0;
    for (int i=1; i<=W; i++)
            if (lang1[i]>0 && lang2[i]>0)
                nowANS++;

    vector<int>::iterator it;
    for (int conf=0; conf<(1 << M); conf++)
    {
        int cnt = 0;
        for (int i=0; i<M; i++)
            if ((conf & (1 << i)))
                for (it=words[3+i].begin(); it!=words[3+i].end(); ++it)
                {
                    lang1[*it]++;
                    if (lang1[*it]==1 && lang2[*it]>0)
                        cnt++;
                }
            else
                for (it=words[3+i].begin(); it!=words[3+i].end(); ++it)
                {
                    lang2[*it]++;
                    if (lang2[*it]==1 && lang1[*it]>0)
                        cnt++;
                }

        ANS = min(ANS, nowANS + cnt);

        for (int i=0; i<M; i++)
            if ((conf & (1 << i)))
                for (it=words[3+i].begin(); it!=words[3+i].end(); ++it)
                    lang1[*it]--;
            else
                for (it=words[3+i].begin(); it!=words[3+i].end(); ++it)
                    lang2[*it]--;
    }

    g << ANS << '\n';
}



int main()
{
#ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
#endif

    f >> T;
    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";
        Read();

        Solve();

        /*int cnt = 0;
        for (int i=1; i<=W; i++)
            if (lang1[i] && lang2[i])
                cnt++;

        g << cnt << '\n';*/
    }

    return 0;
}
