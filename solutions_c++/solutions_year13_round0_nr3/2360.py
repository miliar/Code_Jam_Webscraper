#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>

using namespace std;

typedef long long int tint;
typedef vector<int> vi;
typedef vector<tint> vt;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;


#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define rall(c) (c).rbegin(), (c).rend()
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define si(a) int((a).size())
#define pb push_back
#define mp make_pair

struct fenwick {
	vt op;
	tint siz;

	// arbol para el intervalo (0,n)
	fenwick(tint n) {
		op = vt(n,0);
		siz = 0;
	}

	tint leq(tint key) {
		tint res = 0;
		for (tint i = key; i > 0; i -= i & (-i)) res += op[i];
		return res;
	}

	tint eq(tint key) {
		return leq(key) - leq(key-1);
	}

	void insert(tint key, tint ncopies = 1) {
		for (tint i = key; i < si(op); i += i & (-i)) op[i] += ncopies;
		siz += ncopies;
	}

	tint size() { return siz; }
};

inline bool capicua(tint x) {
    //cout << "capi " << x << " ";
    tint y = x;
    tint r=0;
    while(y>0) {
        r = (r*10) + y%10;
        y/=10;
    }
   // cout << r << endl;
    return x == r;
}

tint f(tint x,bool begin) {
    tint sq = (tint)sqrt(x);

    if (sq * sq == x) return sq;

    if (begin) return sq+1;

    return sq;

}

int main () {
	freopen("C-large-1.in","r",stdin);
	//freopen("out.txt","w",stdout);

    /*tint test = (1LL<<70);
    cout << test << endl;
    return 0;*/

    fenwick F(10000029);
    tint x,y;
    //capicuas de 6 y 7 digitos tales que su cuadrado sea capicua
    /*for(tint a = 1 ; a < 10 ; a++)
        for(tint b = 0; b<10 ; b++)
            for(tint c = 0 ; c<10; c++)
                {
                    x = 100000*a+10000*b+1000*c+100*c+10*b+a;
                    //cout << "x " << x << endl;
                    //cout << "x*x " << x*x << endl;
                    if (capicua(x*x)) {
                        cout << x << endl;
                        F.insert(x);
                    }
                    for(tint d = 0; d < 10 ; d++) {
                        y = ((x/1000) * 10 + d) * 1000 + (x%1000);
                        //cout << y << endl;
                        if (capicua(y*y)) {
                            cout << y << endl;
                            F.insert(y);
                        }
                    }

                }*/

    for(tint a = 1; a<= 9999999 ; a++) {
        if (capicua(a) && capicua(a*a)) {
            F.insert(a);
            cout << a*a << endl;
        }
    }

    tint t,A,B,a,b;



    cin >> t;
    //cout << "**************" << endl;
    forn(caso,t) {
        cin >> A >> B;
        a = f(A,true);
        //cout << a << endl;
        b = f(B,false);
        //cout << b << endl;
        tint res = F.leq(b) - F.leq(a-1);

        cout << "Case #"<<caso+1<<": "<<res<<endl;
    }


    return 0;

}


