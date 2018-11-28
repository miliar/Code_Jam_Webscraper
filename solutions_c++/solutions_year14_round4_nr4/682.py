#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)

typedef long long ll;
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int Ass[15], N, X, T, Ways[10025];
string S[15];

int doTrie(set<int> idx)
{
    set<string> pref;

    for(int i : idx)
    {
        string s = S[i];
        f(i,0,s.length()-1) pref.insert(s.substr(0,i+1));
    }

    return pref.size();
}

void check()
{
    set<int> strings[15];

    f(i,1,N) strings[Ass[i]].insert(i);
    f(i,1,X) if(strings[i].empty()) return;
    int ret = 0;
    f(i,1,X) ret += doTrie(strings[i]);
    Ways[ret+X]++;
}

void process(int p)
{
    if(p > N)
    {
        check();
        return;
    }

    f(i,1,X)
    {
        Ass[p] = i;
        process(p+1);
    }
}

int main()
{
    fin >> T;

    f(t,1,T)
    {
        fin >> N >> X;

        f(i,0,10020) Ways[i] = 0;

        f(i,1,N) fin >> S[i];
        process(1);
        fd(i,10000,0) if(Ways[i])
        {
            cout << "Case #" << t << ": " << i << " " << Ways[i] << "\n";
            fout << "Case #" << t << ": " << i << " " << Ways[i] << "\n";
            break;
        }
    }
}
