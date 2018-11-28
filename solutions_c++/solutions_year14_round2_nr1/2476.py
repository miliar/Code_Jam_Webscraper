#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define foreach(u, o) \
    for (typeof((o).begin()) u = (o).begin(); u != (o).end(); ++u)
const int INF = 2147483647;
const double EPS = 1e-9;
const double pi = acos(-1);
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T mod(T a, T b) { return (a % b + b) % b; }
template <class T> int size(const T &x) { return x.size(); }

string str[100];
int it[100];
int cnt[100];
int T, N;

int next_char()
{
    int average = 0;
    char c = str[0][it[0]];
    int sum = 0;
    memset(cnt, 0, sizeof cnt);
    for(int i = 0; i < N; ++i){
        while(it[i] < str[i].length() && str[i][it[i]] == c){
            //cout << str[i][it[i]];
            it[i]++; cnt[i]++;
        }
        if(!cnt[i]) return -1;
        average += cnt[i];
        //cout << endl;
        //cout << "count " << cnt[i] << endl;
    }
    average /= N;
    //cout << "character " << c << endl;
    //cout << "average " << average << endl;
    for(int i = 0; i < N; ++i){
        //cout << "difference " << abs(average - cnt[i]) << endl;
        sum += abs(average - cnt[i]);
    }
    return sum;
}

bool not_end()
{
    for(int i = 0; i < N; ++i){
        if(it[i] < str[i].length())
            return true;
    }
    return false;
}

int main()
{
    cin >> T;
    int total;
    int next;
    bool fegla;
    for(int t = 0; t < T; ++t){
        fegla = false;
        memset(it, 0, sizeof it);
        total = 0;
        cin >> N;
        cout << "Case #" << t+1 << ": ";
        for(int i = 0; i < N; ++i){
            cin >> str[i];
        }
        while(!fegla && not_end()){
            if((next = next_char()) < 0){
                cout << "Fegla won" << endl;
                fegla = true;
            }
            else 
                total += next;
        }
        if(!fegla){
            cout << total << endl;
        }
    }
}
