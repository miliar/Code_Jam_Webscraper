#include <fstream>
#include <iostream>
#include <vector>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <deque>

using namespace std;

const char infile[] = "input.in";
const char outfile[] = "output.out";

ifstream fin(infile);
ofstream fout(outfile);

const int MAXN = 105;
const int oo = 0x3f3f3f3f;

typedef vector<int> Graph[MAXN];
typedef vector<int> :: iterator It;

const inline int min(const int &a, const int &b) { if( a > b ) return b;   return a; }
const inline int max(const int &a, const int &b) { if( a < b ) return b;   return a; }
const inline void Get_min(int &a, const int b)    { if( a > b ) a = b; }
const inline void Get_max(int &a, const int b)    { if( a < b ) a = b; }

struct Trie {
    Trie *sons[30];
    Trie() {
        memset(sons, 0, sizeof(sons));
    }
};

string a[MAXN];
int N, M;
int answer;
int nr;
int where[MAXN];
int howmany[MAXN];
Trie *Root[MAXN];

inline void Insert(Trie *rada, string s, int &XX) {
    int n = s.length(), c;
    Trie * x = rada;
    for(int i = 0 ; i < n ; ++ i) {
        c = s[i] - 'A';
        if(!x -> sons[c]){
            x -> sons[c] = new Trie(); ++XX;
        }
        x = x->sons[c];
    }
}

inline int getAns() {
    int ret = 0;
    for(int i = 1 ; i <= N ; ++ i)
        Root[i] = new Trie();
    memset(howmany, 0, sizeof(howmany));
    for(int i = 1 ; i <= M ; ++ i) {
        Insert(Root[where[i]], a[i], howmany[where[i]]);
    }
    for(int i = 1 ; i <= N ; ++ i) {
        ret += howmany[i];
        if(howmany[i])
            ++ ret;
    }
    return ret;
}

inline void Back(int k) {
    if(k == M + 1) {
        int aux = getAns();
        if(aux > answer) {
            answer = aux;
            nr = 1;
        } else if(aux == answer)
            ++ nr;
        return;
    }
    for(int i = 1 ; i <= N ; ++ i) {
        where[k] = i;
        Back(k + 1);
    }
}

int main() {
    int T;
    fin >> T;
    for(int test = 1 ; test <= T ; ++ test) {
        fin >> M >> N;
        for(int i = 1  ; i <= M ; ++ i)
            fin >> a[i];
            Back(1);
            fout << "Case #" << test << ": " << answer << ' ' << nr << '\n';
            answer = 0;
            nr = 0;
    }
    return 0;
}
