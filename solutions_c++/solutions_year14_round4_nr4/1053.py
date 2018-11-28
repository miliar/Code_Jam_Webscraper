#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <cctype>

#define FOR(i,n) for(long long int i=0; i<n; i++)
#define MP(a,b) make_pair(a,b)
#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(), a.end())
#define REV(a) reverse(a.begin(), a.end())

#define COND(p,t,f) ((p)?(t):(f))

#define PI 3.14159265

using namespace std;
typedef long long int lint;
typedef unsigned long long int ulint;

void generate (vector<vector<int> >& a, int N, int c) {
    if (c==0) {
        vector <int> c;
        a.PB(c);
        return;
    }
//    cerr << N << " c: " << c << endl;
    generate(a,N,c-1);
    vector<vector<int> >b;
    FOR(i,N) {
        FOR(j,a.size()) {
            b.PB(a[j]);
            b.back().PB(i);
        }
    }
    a=b;
}


int main() {
    int T;
    cin >> T;
    FOR(t,T) {
        int M,N;
        cin >> M >> N;
        vector<string> a(M);
        vector<vector<int> > b;
        FOR(i,M) cin>>a[i];
        generate(b,N,M);

        int maxres = 0;
        int maxrescnt = 0;
        FOR(i,b.size()) {
            vector <vector<string> > v(N);
            FOR(j,M) {
                v[b[i][j]].PB(a[j]);
            }
            int res = 0;
            FOR(j,N) {
                set <string> pref;
                FOR(k,v[j].size()) {
                    string s = v[j][k];
                    while (s!="") {
                        pref.insert(s);
                        s.erase(s.size()-1);
                    }
                    pref.insert(s);
                }
                res += pref.size();

                /*
                bool bbb[50][50] = {{false}};
                //bbb[47][47]=true;
                FOR(k,v[j].size()) {
                    bbb[47][47]=true;
                    FOR(l,v[j][k].size()) {
                        bbb[l][v[j][k][l]-'A']=true;
                    }
                }
                FOR(mm,50) FOR(nn,50) res+=COND(bbb[mm][nn],1,0);*/

            }
            if (res>maxres) {
                maxres=res;
                maxrescnt=0;
            }
            else if (res==maxres) {
                maxrescnt++;
            }
        }
/*
        FOR(i,b.size()) {
            FOR (j, b[0].size()) cerr << b[i][j];
            cerr << endl;
        }
*/
        cout << "Case #" << t+1 << ": ";
        cout << maxres << " " << maxrescnt+1 << endl;
    }

}
