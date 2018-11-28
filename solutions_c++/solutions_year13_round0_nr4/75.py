#include <string>
#include <iostream>
#include <vector>
#include <utility>
#include <cstdio>
#include <sstream>
#include <map>
using namespace std;

void init()
{
}


vector<int> initKeys;
int K, N;
vector<int> openKey;
vector<int> keys[500];

bool caled[1 << 20];
bool isok[1 << 20];
vector<int> path[1 << 20];

void read()
{
    cin >> K >> N;
    initKeys.resize(K);
    for (int i = 0; i < K; ++i) cin >> initKeys[i];
    
    openKey.resize(N);
    for (int i = 0; i < N; ++i)
    {
        cin >> openKey[i];
        int Ki;
        cin >> Ki;
        keys[i].resize(Ki);
        for (int j = 0; j < Ki; ++j) cin >> keys[i][j];
    }
}

bool getF(int state)
{
    if (caled[state]) return isok[state];
    caled[state] = true;
    bool & ret = isok[state];
    path[state].clear();
    ret = false;
    
    if (state == (1 << N) - 1) return ret = true;
    
    map<int, int> nowKeys;
    for (int i = 0; i < initKeys.size(); ++i) nowKeys[initKeys[i]]++;
    for (int i = 0; i < N; ++i)
        if (state & (1 << i))
        {
            nowKeys[openKey[i]]--;
            for (int j = 0; j < keys[i].size(); ++j)
                nowKeys[keys[i][j]]++;
        }
    
    for (int i = N - 1; i >= 0; --i)
        if ((state & (1 << i)) == 0)
        {
            int newstate = state + (1 << i);
            if (nowKeys[openKey[i]] > 0)
            {
                bool newF = getF(newstate);
                if (newF)
                {
                    ret = true;
                    path[state] = path[newstate];
                    path[state].push_back(i);
                }
            }
        }
    return ret;
}

string deal()
{
    memset(caled, false, sizeof(caled));
    bool ans = getF(0);
    if (!ans) return "IMPOSSIBLE";
    
    ostringstream ostr;
    for (int i = (int) path[0].size() - 1; i >= 0; --i)
        ostr << path[0][i] + 1 << " ";
    return ostr.str();
}

int main()
{
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/QUAL/d.in", "r", stdin);
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/QUAL/d.out", "w", stdout);
    
    init();
    
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test)
    {
        read();
        cerr << "Running " << test << endl;
        cout << "Case #" << test << ": " << deal() << endl;
    }
    return 0;
}