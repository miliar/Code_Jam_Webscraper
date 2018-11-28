#undef __STRICT_ANSI__
#include <fstream>
#include <cstring>
#include <iomanip>
#include <vector>
#include <unordered_map>

#define maxn 110
#define inf 200000

using namespace std;

ifstream fin("test.in");
ofstream fout("test.out");

int n,rez,ans;
char s[100010];
vector<int> v[30];
bool English[100010], French[100010];
unordered_map<string,int> parser;
int t;

void parse (char s[], vector<int> &v)
{
    int p = 0;
    int len = strlen(s);
    string w;
    for (; p < len; ++p)
    {
        if (s[p] == ' ')
        {
            if (parser.find(w) != parser.end())
            {
                v.push_back(parser[w]);
            }
            else
            {
                parser[w] = ++t;
                v.push_back(t);
            }
            w = "";
        }
        else
        {
            w += s[p];
        }
    }

    if (w != "")
    {
        if (parser.find(w) != parser.end())
            {
                v.push_back(parser[w]);
            }
            else
            {
                parser[w] = ++t;
                v.push_back(t);
            }
            w = "";
    }
}

void back(int k)
{
    if (k == n+1)
    {
        rez = min(rez, ans);
        return;
    }

    int ret = ans;
    vector<bool> ok(v[k].size());

    for (int i = 0; i < v[k].size(); ++i)
    {
        if (!French[v[k][i]])
        {
            French[v[k][i]] = 1;
            ok[i] = 1;

            if (English[v[k][i]])
            {
                ++ans;
            }
        }
        else ok[i] = 0;
    }

    back(k+1);

    ans = ret;
    for (int i = 0; i < ok.size(); ++i)
    {
        if (ok[i])
            French[v[k][i]] = 0;
    }

    for (int i = 0; i < v[k].size(); ++i)
    {
        if (!English[v[k][i]])
        {
            English[v[k][i]] = 1;
            ok[i] = 1;

            if (French[v[k][i]])
            {
                ++ans;
            }
        }
        else ok[i] = 0;
    }

    back(k+1);

    ans = ret;
    for (int i = 0; i < ok.size(); ++i)
    {
        if (ok[i])
            English[v[k][i]] = 0;
    }
}

long double solve()
{
    t = 0;
    parser.clear();

    fin >> n;

    fin.getline(s,10000);

    for (int i = 1; i <= n; ++i)
    {
        v[i].clear();
        fin.getline(s,100000);
        parse(s,v[i]);
    }

    ans = 0;
    rez = inf;
    memset(English,0,sizeof(English));
    memset(French,0,sizeof(French));

    for (int i = 0; i < v[1].size(); ++i)
    {
        if (!English[v[1][i]])
            English[v[1][i]] = 1;
    }

    for (int i = 0; i < v[2].size(); ++i)
    {
        if (!French[v[2][i]])
        {
            if (English[v[2][i]])
                ++ans;
            French[v[2][i]] = 1;
        }
    }

    back(3);

    return rez;
}

void reset()
{
}

int main()
{
    int test;

    fin >> test;

    for (int k = 1; k <= test; ++k)
    {
        reset();
        int answer = solve();
        fout << "Case #" << k << ": ";
        fout << answer;
        fout << "\n";
    }
}
