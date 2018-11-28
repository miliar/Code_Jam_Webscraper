#include <fstream>
#include <cstring>
using namespace std;

int tests, test, n, i, j, k, ok, cnt[200][200], total[200];
string s, t, compareTo;
int main()
{
    ifstream fi("test.in");
    ofstream fo("test.out");
    fi >> tests;
    for(int test = 1; test <= tests; test++)
    {
        fi >> n;
        memset(total, 0, sizeof(total));
        memset(cnt, 0, sizeof(cnt));
        for(i = 1, ok = 1; ok and i <= n; i++)
        {
            fi >> s;
            string t = s.substr(0, 1);
            int l = 1;
            k = 1;
            for(j = 1; j < s.length(); j++)
                if(s[j] != s[j-1])
                {
                    cnt[l][k]++;
                    total[l] += k;
                    k = 1;
                    t += s[j];
                    l++;
                } else k++;

            cnt[t.length()][k]++;
            total[t.length()] += k;

            if(i == 1) compareTo = t;
            if(t != compareTo) ok = 0;
        }
        fo << "Case #" << test << ": ";
        if(!ok) fo << "Fegla won\n";
        else
        {
            int sol = 0;
            for(i = 1; i <= compareTo.length(); i++)
            {
                int minSol = total[i] - n;
                int cost = total[i] - n;
                int nr = cnt[i][1];
                for(j = 2; j <= 100; j++)
                {
                    cost += nr;
                    cost -= n - nr;
                    nr += cnt[i][j];
                    if(minSol > cost) minSol = cost;
                    if(nr >= n) break;
                }
                sol += minSol;
            }
            fo << sol << "\n";
        }
    }
    return 0;
}
