#include "bits/stdc++.h"
#define BLANK 0
#define UP 1
#define DOWN 2
#define LEFT 3
#define RIGHT 4
using namespace std;

int t;
int mapp[110][110];
int name[110][110];

void work()
{
    int cnt = 0;
    int r, c;
    cin >> r >> c;
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            name[i][j] = -1;
    for (int i = 0; i < r; ++i)
    {
        string s;
        cin >> s;
        for (int j = 0; j < c; ++j)
        {
            switch (s[j])
            {
            case '.':
                mapp[i][j] = BLANK;
                break;
            case '^':
                mapp[i][j] = UP;
                name[i][j] = cnt++;
                break;
            case 'v':
                mapp[i][j] = DOWN;
                name[i][j] = cnt++;
                break;
            case '<':
                mapp[i][j] = LEFT;
                name[i][j] = cnt++;
                break;
            case '>':
                mapp[i][j] = RIGHT;
                name[i][j] = cnt++;
                break;
            default:
                1/0;
            }
        }
    }

    vector<int> ue[cnt];
    vector<int> out[cnt];
    //vector<int> in[cnt];
    for (int i = 0; i < r; ++i)
    {
        for (int j = 0; j < c; ++j)
        {
            if (mapp[i][j] == BLANK)
                continue;

                for (int k = 0; k < r; ++k)
                {
                    if (k == i || mapp[k][j] == BLANK) continue;
                    ue[name[i][j]].push_back(name[k][j]);
                    if (mapp[i][j] == UP && k < i)
                    {
                        out[name[i][j]].push_back(name[k][j]);
                     //   in[name[k][j]].push_back(name[i][j]);
                    }
                    else if (mapp[i][j] == DOWN && k > i)
                    {
                        out[name[i][j]].push_back(name[k][j]);
                      //  in[name[k][j]].push_back(name[i][j]);
                    }
                }
                for (int k = 0; k < c; ++k)
                {
                    if (k == j || mapp[i][k] == BLANK) continue;
                    ue[name[i][j]].push_back(name[i][k]);
                    if (mapp[i][j] == LEFT && k < j)
                    {
                        out[name[i][j]].push_back(name[i][k]);
                 //       in[name[i][k]].push_back(name[i][j]);
                    } 
                    else if (mapp[i][j] == RIGHT && k > j)
                    {
                        out[name[i][j]].push_back(name[i][k]);
                   //     in[name[i][k]].push_back(name[i][j]);
                    }
                }
        }
    }
    
    for (int i = 0; i < cnt; ++i)
    {
        if (ue[i].size() == 0)
        {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }


    int ans = 0;
    for (int i = 0; i < cnt; ++i)
    {
        if (out[i].size() == 0)
            ++ans;
    }
    cout << ans << endl;
    return;
}

int main()
{
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        work();
    }
    return 0;
}
