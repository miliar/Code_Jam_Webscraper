#include <string>
#include <iostream>
#include <vector>
#include <utility>
#include <cstdio>
#include <sstream>
#include <cmath>
#include <map>
using namespace std;

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <utility>
#include <sstream>
#include <bitset>
#include <stdio.h>
using namespace std;

#define DEBUG 0
#define debug1(x) if (DEBUG) cout << #x" = " << x << endl;
#define debug2(x, y) if (DEBUG) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) if (DEBUG) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) if (DEBUG) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;

template <class T>
ostream & operator << (ostream & out, const vector<T> & data)
{ out << "["; for (int i = 0; i < data.size(); ++i) out << data[i] << (i == data.size() - 1 ? "" : ","); out << "]"; return out; }

template <class T>
ostream & operator << (ostream & out, const set<T> & s)
{ out << "{"; for (typename set<T>::iterator itr = s.begin(); itr != s.end(); ++itr) out << *itr << " "; out << "}"; return out; }

template <class T>
ostream & operator << (ostream & out, const multiset<T> & s)
{ out << "{"; for (typename multiset<T>::iterator itr = s.begin(); itr != s.end(); ++itr) out << *itr << " "; out << "}"; return out; }

template <class T1, class T2>
ostream & operator << (ostream & out, const pair<T1, T2> & p)
{ out << "(" << p.first << "," << p.second << ")"; return out; }

template <class T1, class T2>
ostream & operator << (ostream & out, const map<T1, T2> & m)
{
    for (typename map<T1, T2>::const_iterator itr = m.begin(); itr != m.end(); ++itr)
        out << itr->first << "->" << itr->second << " ";
    return out;
}

int R, N, M, K;

struct State
{
    vector<int> nums;
    map<long long, double> generateProb;
    
    void generate()
    {
        generateProb.clear();
        int n = (int) nums.size();
        for (int s = 0; s < (1 << n); ++s)
        {
            long long nowMulti = 1;
            for (int i = 0; i < n; ++i)
                if (s & (1 << i))
                    nowMulti *= nums[i];
            generateProb[nowMulti] += 1.0 / (1 << n);
        }
    }
    
    
};

void generateStates(vector<int>& nums, int offset, int begin, vector<State>& states)
{
    if (offset == nums.size())
    {
        State s;
        s.nums = nums;
        states.push_back(s);
        states.back().generate();
        return;
    }
    
    for (int i = begin; i <= M; ++i)
    {
        nums[offset] = i;
        generateStates(nums, offset + 1, i, states);
    }
}

vector<State> states;

void init()
{
    cin >> R >> N >> M >> K;
    vector<int> nums(N);
    generateStates(nums, 0, 2, states);
    
    for (int i = 0; i < states.size(); ++i)
    {
        //cout << states[i].nums << endl;
        //cout << states[i].generateProb << endl;
    }
}

string deal()
{
    string answer = "\n";
    for (int iter = 0; iter < R; ++iter)
    {
        vector<long long> ks(K);
        for (int i = 0; i < K; ++i) cin >> ks[i];
        
        double maxprob = 0;
        int maxStateOffset = 0;
        for (int i = 0; i < states.size(); ++i)
        {
            double nowprob = 1.0;
            for (int j = 0; j < K; ++j)
                nowprob *= states[i].generateProb[ks[j]];
            if (nowprob > maxprob)
            {
                maxprob = nowprob;
                maxStateOffset = i;
            }
        }
        
        string ans = "";
        for (int i = 0; i < states[maxStateOffset].nums.size(); ++i)
            ans += string(1, '0' + states[maxStateOffset].nums[i]);
        answer += ans + "\n";
    }
    return answer;
}

int main()
{
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/Round1A/c.in", "r", stdin);
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/Round1A/c.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test)
    {
        init();
        cout << "Case #" << test << ": " << deal() << endl;
    }
    return 0;
}