#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

//BEGINTEMPLATE_BY_SCORPIOLIU
const double PI  = acos(-1.0);
const double EPS = 1e-11;
const double INF  = 1E200;

typedef long long int64;
typedef unsigned long long uint64;

typedef pair<int,int> ipair;
#define MP(X,Y) make_pair(X,Y)
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))

#define REP(i,a) for(int i=0;i<int(a);++i)
#define REP2(i,n,m) for(int i=n;i<(int)(m);++i)
#define FORE(it,a) for (typeof((a).begin()) it=(a).begin();it!=(a).end();++it)
#define ALL(a) (a).begin(),(a).end()
//ENDEMPLATE_BY_SCORPIOLIU

//#define SMALL
#define LARGE

bool check(vector<vector<int> >a, vector<vector<bool> >c, int m, int n){
    for (int i = 0; i<m ;i++){
        int h = -1;
        for (int j = 0; j< n; j++) {
            if (a[i][j] > h) {
                h = a[i][j];
            }
        }
        for (int j = 0; j< n; j++) {
            if (a[i][j] == h)
            {
                c[i][j] = true;
            }
        }
    }

    for (int i = 0; i<n ;i++){
        int h = -1;
        for (int j = 0; j<m; j++) {
            if (a[j][i] > h) {
                h = a[j][i];
            }
        }
        for (int j = 0; j< m; j++) {
            if (a[j][i] == h)
            {
                c[j][i] = true;
            }
        }
    }


    for (int i = 0; i<m ;i++){
        for (int j = 0; j< n; j++) {
            if (!c[i][j]) {
                return false;
            }
        }
    }
    return true;
}

int main()
{
#ifdef SMALL
    //ifstream fin("C-small-practice.in");ofstream fout("C-small-practice.out");
    //ifstream fin("C-small-attempt0.in");ofstream fout("C-small-attempt0.out");
    freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("C-large-practice.in");ofstream fout("C-large-practice.out");
    //ifstream fin("C-large.in");ofstream fout("C-large.out");
    freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
#endif
    char tb[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
    'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    int N;
    string s;
    cin>>N;
    getline(cin, s);
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        vector<vector<int> >a;
        vector<int>b;
        vector<vector<bool> >c;
        vector<bool>d;
        int h, m,n;
        cin>>m>>n;
        for (int i = 0; i <m ;i++){
            for (int j = 0; j< n; j++) {
                cin>>h;
                b.push_back(h);
                d.push_back(false);

            }
            a.push_back(b);
            c.push_back(d);
            b.clear();
            d.clear();
        }
        if (check(a, c, m, n)) {
            cout<<"YES";
        } else {
            cout<<"NO";
        }
        //////////////////////////////////////
        cout<<endl;
    }


    return 0;
}
