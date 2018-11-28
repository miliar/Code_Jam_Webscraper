#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<queue>
#include<complex>
#include<set>
#include<map>
#include<sstream>
#include<string>
#include<deque>
#include<sys/time.h>
#include<fstream>
#include<bitset>
#include<cstring>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define dforn(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

int main() {
    int T;
    cin>>T;
    forn(t,T) {
        int R,C;
        cin>>R>>C;
        vector<string> b(R);
        forn(i,R) {
            cin>>b[i];
        }
        vector<vector<int> > fa(R, vector<int>(C));
        vector<vector<int> > fd(R, vector<int>(C));
        vector<vector<int> > ca(R, vector<int>(C));
        vector<vector<int> > cd(R, vector<int>(C));
        int res = 0;
        bool possible = true;
        forn(i,R) {
            forn(j, C - 1) {
                fa[i][j + 1] = fa[i][j];
                if(b[i][j] != '.') fa[i][j + 1]++;
            }
        }
        forn(j,C) {
            forn(i, R - 1) {
                ca[i + 1][j] = ca[i][j];
                if(b[i][j] != '.') ca[i + 1][j]++;
            }
        }
        forn(i,R) {
            dforn(j, C) if(j) {
                fd[i][j - 1] = fd[i][j];
                if(b[i][j] != '.') fd[i][j - 1]++;
            }
        }
        forn(j,C) {
            dforn(i, R) if(i) {
                cd[i - 1][j] = cd[i][j];
                if(b[i][j] != '.') cd[i - 1][j]++;
            }
        }
        forn(i,R) forn(j,C) if(b[i][j] != '.') {
            if(fa[i][j] == 0 && fd[i][j] == 0 &&
                ca[i][j] == 0 && cd[i][j] == 0) {
                possible = false;
            } else {
                if((b[i][j] == '^' && ca[i][j] == 0) ||
                   (b[i][j] == 'v' && cd[i][j] == 0) ||
                   (b[i][j] == '<' && fa[i][j] == 0) ||
                   (b[i][j] == '>' && fd[i][j] == 0)) {
                    res++;
                }
            }
        }
        if(!possible) {
             cout<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;
        } else cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
    return 0;
}
