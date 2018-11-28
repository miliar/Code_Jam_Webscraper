#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c, x) ((c).find(x) != (c).end())
#define cpresent(c, x) (find(all(c), x) != (c).end())
#define REP(i, n) for(int i = 0; i < (n); i++)
#define REPD(i, n) for(int i = (n)-1; i >= 0; i--)
#define FOR(i, a, b) for(int i = (a); i <= (b); i++)
#define FORD(i, a, b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define CHECK(S, j) (S & (1 << j))
#define SET(S, j) (S |= (1 << j))
#define SETALL(S, j) (S = (1 << j)-1)
#define UNSET(S, j) (S &= ~(1 << j))
#define TOGGLE(S, j) (S ^= (1 << j))
#define LL long long
#define PI acos(-1)
template<class T>string tostring(T t){stringstream s;s<<t;return s.str();}

//GCJ Includes
#include <fstream>

int main() {
    ifstream fin("D-large.in");
    ofstream fout("output.out");
    int t;
    fin >> t;
    REP(i, t){
        int N;
        fin >> N;
        vector<double> naomi(N);
        vector<double> ken(N);
        REP(j, N)
            fin >> naomi[j];
        REP(j, N)
            fin >> ken[j];
        sort(all(naomi));
        sort(all(ken));
        vector<double> cnaomi(naomi), cken(ken);
        int war = 0;
        REP(j, sz(naomi)){
            REP(k, sz(ken)){
                if(ken[k] > naomi[j]){
                    war++;
                    ken.erase(ken.begin()+k);
                    naomi.erase(naomi.begin()+j);
                    j--;
                    break;
                }
            }
        }
        war = N - war;
        int dwar = 0;
        while(sz(cnaomi)){
            if(cnaomi[0] < cken[0]){
                cnaomi.erase(cnaomi.begin());
                cken.erase(cken.begin()+sz(cken)-1);
            }else{
                dwar++;
                cnaomi.erase(cnaomi.begin());
                cken.erase(cken.begin());
            }
        }
        fout << "Case #"<< i+1 <<": " <<dwar << " " << war << endl;
    }
    return 0;
}
