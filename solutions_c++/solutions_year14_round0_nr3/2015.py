#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)

int mipc(int x)
{
    if (x == 0) return 0;
    else return __builtin_popcount(x);
}

int main()
{
    int TT; cin >> TT;
    forn(tt,TT)
    {
        int R,C,M; cin >> R >> C >> M;
        cout << "Case #" << tt+1 << ":" << endl;
        if (M == R*C - 1)
        {
            forn(i,R)
            {
                forn(j,C)
                if (i == 0 && j == 0)
                    cout << "c";
                else
                    cout << "*";
                cout << endl;
            }
        }
        else
        {
            static char tab[8][8];
            static char num[8][8];
            static char pin[8][8];
            bool haySol = false;
            
            forn(mask, (1<<(R*C)))
            if (mipc(mask) == M)
            {
                forn(i,R)
                forn(j,C)
                    tab[i][j] = ((mask & (1 << (C * i + j))) != 0);
                forn(i,R)
                forn(j,C)
                {
                    num[i][j] = 0;
                    forsn(di, -1, 2)
                    forsn(dj, -1, 2)
                    {
                        int ni = i+di;
                        int nj = j+dj;
                        if (0 <= ni && ni < R &&
                            0 <= nj && nj < C)
                            num[i][j] += tab[ni][nj];
                    }
                }
                memset(pin,0,sizeof(pin));
                int ox = 0,oy = 0;
                forn(i,R)
                forn(j,C)
                if (num[i][j] == 0)
                {
                    ox = i;
                    oy = j;
                    vector<pair<int,int> > pending;
                    pending.push_back(make_pair(i,j));
                    pin[i][j] = 1;
                    while (!pending.empty())
                    {
                        int x = pending.back().first;
                        int y = pending.back().second;
                        pending.pop_back();
                        forsn(di, -1, 2)
                        forsn(dj, -1, 2)
                        {
                            int ni = x+di;
                            int nj = y+dj;
                            if (0 <= ni && ni < R &&
                                0 <= nj && nj < C && !pin[ni][nj])
                            {
                                pin[ni][nj] = 1;
                                if (num[ni][nj] == 0)
                                    pending.push_back(make_pair(ni,nj));
                            }
                        }
                    }
                    goto superbreak;
                }
superbreak:;
                bool anda = true;
                forn(i,R)
                forn(j,C)
                if (tab[i][j] == 0 && !pin[i][j])
                {
                    anda = false;
                    break;
                }
                if (anda)
                {
                    forn(i,R)
                    {
                        forn(j,C)
                        if (tab[i][j])
                            cout << "*";
                        else if (ox == i &&  oy == j)
                            cout << "c";
                        else
                            cout << ".";
                        cout << endl;
                    }
                    haySol = true;
                    break;
                }
            }
            if (!haySol)
                cout << "Impossible" << endl;
        }
        
        //cout << res << endl;
    }
    return 0;
}
