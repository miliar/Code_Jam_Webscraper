#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<ctime>
#include<string>
#include<vector>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<bitset>
#include<algorithm>
#define INF (1 << 30)
#define pb push_back
#define mkp make_pair
#define pii pair<int, int>
#define ll long long
#define nxt (*it)
#define type int
#define FOR(i,a,b)\
   for(int i=a; i<=b; ++i)
#define FORR(i,a,b)\
   for(int i=a; i>=b; --i)
#define ALLR(g) \
   for(typeof(g.rbegin()) it=g.rbegin(); it!=g.rend(); ++it)
#define ALL(g)\
   for(typeof(g.begin()) it=g.begin(); it!=g.end(); ++it)
using namespace std;

int T;

ll sq[] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
int sz = 38;

ll A, B;

inline int start(){
    FOR(i,0,sz)
        if(sq[i] * sq[i] >= A)
            return i;
    return INF;
}

inline int finish(){
    FORR(i,sz,0)
        if(sq[i] * sq[i] <= B)
            return i;
    return -INF;
}

int main(){
    //ifstream fin("in.txt");
    //ofstream fout ("out.txt");

    cin >> T;

    int s, f, r;
    FOR(t,1,T){
        cin >> A >> B;
        s = start();
        f = finish();

        r = f - s + 1;

        if(r < 0)
            r = 0;

        cout << "Case #" << t << ": " << r << '\n';
    }

    return 0;
}
