#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <queue>

using namespace std;

const int maxN = 100;
const int maxM = 5;
const int maxRetry = 28571;

int n, m;
int par[maxN];
char c[maxN];
vector<int> children[maxN];
vector<int> descendants[maxN];
int topo[maxN];
int perm[maxN];

string s[maxM];
int s_cnt[maxM];

int main()
{
    int t, ct;
    mt19937_64 rng(0xc0de1ab);

    cin >> ct;
    for (t = 1; t <= ct; t++)
    {
        cin >> n;
        for (int i = 0; i < n; i ++)
        {
            cin >> par[i];

            par[i] --;
        }
        for (int i = 0; i < n; i ++)
        {
            cin >> c[i];
        }

        for (int i = 0; i < n; i ++)
        {
            children[i].clear();
            descendants[i].clear();
        }

        for (int i = 0; i < n; i ++)
        {
            if (par[i] != -1)
            {
                children[par[i]].push_back(i);
            }
        }

        {
            queue<int> q;
            for (int i = 0; i < n; i ++)
            {
                if (par[i] == -1)
                {
                    q.push(i);
                }
            }

            int topo_len = 0;
            while (!q.empty())
            {
                int cur = q.front();
                q.pop();
                topo[topo_len ++] = cur;
                for (int x : children[cur])
                {
                    q.push(x);
                }
            }
        }

        for (int j = n - 1; j >= 0; j --)
        {
            int i = topo[j];
            for (x : children[i])
            {
                descendants[i].push_back(x);
                for (y : descendants[x])
                {
                    descendants[i].push_back(y);
                }
            }
        }

        cin >> m;
        for (int i = 0; i < m; i ++)
        {
            cin >> s[i];
            s_cnt[i] = 0;
        }

        for (int i = 0; i < maxRetry; i ++)
        {
            for (int j = 0; j < n; j ++)
            {
                perm[j] = j;
                int p = uniform_int_distribution<int>(0, j)(rng);
                swap(perm[p], perm[j]);
            }

            for (int j = 0; j < n; j ++)
            {
                int k = topo[j];

                int min = perm[k];
                int min_id = k;
                for (int x : descendants[k])
                {
                    if (perm[x] < min)
                    {
                        min = perm[x];
                        min_id = x;
                    }
                }

                swap(perm[k], perm[min_id]);
            }

            string str(n, ' ');
            for (int j = 0; j < n; j ++)
            {
                str[perm[j]] = c[j];
            }

            for (int j = 0; j < m; j ++)
            {
                if (str.find(s[j]) != string::npos)
                {
                    s_cnt[j] ++;
                }
            }
        }

        cout << "Case #" << t << ":";
        for (int i = 0; i < m; i ++)
            cout << " " << s_cnt[i] / (double)maxRetry;
        cout << endl;
    }

    return 0;
}
