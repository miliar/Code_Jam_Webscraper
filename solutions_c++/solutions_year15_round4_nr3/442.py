#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <map>

using namespace std;

int T, N;
char c[100000];

vector<int> v[30];

map<string, int> m; int mn;

bool s[3000];
bool r[3000];

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);

    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        m.clear();
        mn = 0;

        scanf("%d", &N);

        for(int Ni = 0; Ni < N; Ni++)
        {
            v[Ni].clear();
            scanf(" %[^\n]", c);

            char *p = strtok(c, " ");

            while( p != NULL )
            {
                string q = string(p);
                if( m.find(q) == m.end() ) m[q] = ++mn;

                v[Ni].push_back(m[q] );

                p = strtok(NULL, " ");
            }
        }

        int Ans = 1000000000;

        for(int i = 0; i < (1<<N-2); i++)
        {
            fill(s+1, s+mn+1, false);
            fill(r+1, r+mn+1, false);

            for(int vi = 0; vi < v[0].size(); vi++)
                s[v[0][vi] ] = true;

            for(int vi = 0; vi < v[1].size(); vi++)
                r[v[1][vi] ] = true;

            int b = 1;

            for(int Ni = 2; Ni < N; Ni++)
            {

                if( b&i )
                {
                    for(int vi = 0; vi < v[Ni].size(); vi++)
                        s[v[Ni][vi] ] = true;
                }
                else
                {
                    for(int vi = 0; vi < v[Ni].size(); vi++)
                        r[v[Ni][vi] ] = true;
                }

                b *= 2;
            }

            int cnt = 0;

            for(int mi = 1; mi <= mn; mi++)
                if( s[mi] && r[mi] ) cnt++;

            Ans = min(Ans, cnt);
        }

        printf("Case #%d: %d\n", Ti, Ans);
    }
}
