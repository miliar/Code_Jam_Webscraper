#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define EPS 1.0e-6
#define INF 10000000
#define DIV 1000000007

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

long long fatorial[105];

void pre_calc()
{
    fatorial[0] = 1LL;
    for(long long i=1LL; i<105; i++)
        fatorial[i] = (i*fatorial[i-1]) % DIV;
}

class UnionFind {
private:
  vector<int> p, rank, setSize;
  int numSets;
public:
  UnionFind(int N) {
    setSize.assign(N, 1); numSets = N; rank.assign(N, 0);
    p.assign(N, 0); for (int i = 0; i < N; i++) p[i] = i; }
  int findSet(int i) { return (p[i] == i) ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }
  void unionSet(int i, int j) {
    if (!isSameSet(i, j)) { numSets--;
    int x = findSet(i), y = findSet(j);

    if (rank[x] > rank[y]) { p[y] = x; setSize[x] += setSize[y]; }
    else                   { p[x] = y; setSize[y] += setSize[x];
                             if (rank[x] == rank[y]) rank[y]++; } } }
  int numDisjointSets() { return numSets; }
  int sizeOfSet(int i) { return setSize[findSet(i)]; }
};

char s[105][105];
int len[105];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    pre_calc();

    int T;
    int idx, ocor;
    bool achou, impossivel;
    long long resp;

    int n, inicio, meio, fim, todo;

    scanf("%d", &T);
    for(int ncaso=1; ncaso<=T; ncaso++)
    {
        scanf("%d", &n);
        FOR(i,0,n) scanf("%s", s[i]), len[i] = strlen(s[i]);

        impossivel = false;

        resp = 1LL;

        UnionFind UF(n);
        for(char c='a'; c<='z'; c++)
        {
            vi v;
            inicio = 0; meio = 0; fim = 0; todo = 0;
            FOR(i,0,n)
            {
                achou = false;
                if (s[i][0] == c)
                {
                    achou = true;
                    idx = 1;
                    while(s[i][idx] == c && idx<len[i]) idx++;
                    if (idx == len[i]) todo++;
                    else
                    {
                        idx++;
                        while(idx<len[i])
                        {
                            if (s[i][idx] == c) impossivel=true;
                            idx++;
                        }
                        inicio++;
                    }
                }
                else if (s[i][len[i]-1] == c)
                {
                    achou = true;
                    idx = len[i]-2;
                    while(s[i][idx] == c && idx>=0) idx--;
                    if (idx == -1) todo++;
                    else
                    {
                        idx--;
                        while(idx>=0)
                        {
                            if (s[i][idx] == c) impossivel=true;
                            idx--;
                        }
                        fim++;
                    }
                }
                else
                {
                    ocor = 0;
                    FOR(j,1,len[i]-1)
                    {
                        if (s[i][j] == c)
                        {
                            achou = true;
                            meio++;
                            ocor++;
                            while(s[i][j] == c && j<len[i]) j++;
                        }
                    }
                    if (ocor > 1) impossivel = true;
                }

                if (achou) v.push_back(i);
            }

            FOR(i,1,v.size())
            {
                if (UF.isSameSet(v[i],v[0])) impossivel = true;
                else UF.unionSet(v[i],v[0]);
            }

            if (inicio > 1) impossivel = true;
            if (fim > 1) impossivel = true;
            if (meio && (inicio || fim || todo)) impossivel = true;
            if (impossivel) break;
            else
            {
                resp = (resp * fatorial[todo]) % DIV;
            }
        }

        resp = (resp * fatorial[UF.numDisjointSets()]) % DIV;

        if (impossivel) printf("Case #%d: 0\n", ncaso);
        else printf("Case #%d: %lld\n", ncaso, resp);
    }

    return 0;
}
