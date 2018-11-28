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

#define SMALL
//#define LARGE

bool check(int a){
    stringstream ss;
    string tmp, tmp2;
    ss<<a;
    ss>>tmp;
    tmp2 = tmp;
    reverse(tmp.begin(), tmp.end());
    ss.clear();
    return tmp2 == tmp;
}

int main()
{
#ifdef SMALL
    //ifstream fin("C-small-practice.in");ofstream fout("C-small-practice.out");
    //ifstream fin("C-small-attempt0.in");ofstream fout("C-small-attempt0.out");
    freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("C-large-practice.in");ofstream fout("C-large-practice.out");
    //ifstream fin("C-large.in");ofstream fout("C-large.out");
    freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
#endif
    char tb[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
    'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    int N;
    string s;
    bool t[2000];
    memset(t, 0, sizeof(t));

    for (int i = 0 ; i< 100;i ++)
    {
        if (check(i)) {
            if (check(i*i)) {
                t[i*i] = true;
            }
        }
    }
    cin>>N;
    getline(cin, s);
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int a, b, cnt=0;
        cin>>a>>b;

        for (int i=a; i<=b; i++)
        {
            if (t[i]) {
                cnt ++;
            }
        }
        cout<<cnt;
        //////////////////////////////////////
        cout<<endl;
    }


    return 0;
}
