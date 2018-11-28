#pragma comment(linker, "/STACK:33554432")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <ctime>
#include <memory.h>

using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define ABS(n) ((n)<0 ? -(n) : (n))
#define SQR(a) (a)*(a)
#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define COPY(a,b) memcpy(a,b,sizeof (b));
#define SI(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define y1 yyyyy1
#define prev prevvvvv
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-8;
const int INF = (1<<30)-1;
const int P = 1000000007;

struct Node{
    map<char, int> way;
};
class Trie {
    vector<map<char,int> > nodes;
public:
    Trie() {
        nodes.push_back(map<char,int>());
    }
    void add(string s) {
        int curr = 0;
        REP(i,s.size()) {
            if (nodes[curr].find(s[i]) != nodes[curr].end()) {
                curr = nodes[curr][s[i]];
            } else {
                nodes[curr][s[i]] = nodes.size();
                nodes.push_back(map<char,int>());
                curr = nodes.size()-1;
            }
        }
    }
    int size() {
        return nodes.size();
    }
};

int tc, n, m;
string s[100];
int num[20];
int max_size;
int max_count;

void check() {
    int cnt[10];
    memset(cnt, 0, sizeof(cnt));
    REP(i,n) cnt[num[i]]++;
    REP(i,m) if (cnt[i] == 0) return;
    int total_size = 0;
    REP(i,m) {
        Trie t;
        REP(j,n) if (num[j] == i) t.add(s[j]);
        total_size += t.size();
    }
    if (total_size > max_size) {
        max_size = total_size;
        max_count = 1;
    } else if (total_size == max_size) {
        max_count += 1;
    }
}

void recit(int curr, int total) {
    if (curr == n) {
        check();
        return;
    }
    REP(i,total) {
        num[curr] = i;
        recit(curr+1, total);
    }
}

void fun() {
    max_size = 0;
    max_count = 0;
    recit(0, m);
}

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

    cin >> tc;
    REP(ic,tc) {
        cin >> n >> m;
        REP(i,n) cin >> s[i];
        fun();
        cout << "Case #" << ic+1 << ": " << max_size << " " << max_count << endl;
    }

	return 0;
};