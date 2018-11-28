#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>


using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()

#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
    if (fabs(a - b) < eps)
        return 0;
    return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int I, J;

inline bool val(const int &i, const int &j) {
    if (i < 0 || j < 0 || i >= I || j >= J)
        return false;
    return true;
}

inline long long isItPrime(long long n) {
    //cout << endl;
    long long i;
    if( n <= 1 )
        return false;
    long long sss = sqrt(n);
    for( i = sss ; i >= 2; i-- ) {
        //use a recursive call to check for prime-ness first
        // cout << i << " " << n << endl;
        if(n % i == 0 )
            return i;
    }
    return -1;
}
/*
 
 */

int N;
int main(int argc, char *args[]) {
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("small.in","rt",stdin);
        freopen("small.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("large.in","rt",stdin);
        freopen("large.out","wt",stdout);
    }
    else {
        freopen("a.txt", "rt", stdin);
    }
    cin>>N;
    int a,b,c;
    int d,e,f,z;
    long long tmp;
    bool isPrime;
    int nbSolutions;
    long long dividors[9];
    rep2(nn,1,N+1) {
        printf("Case #%d: \n", nn);
        nbSolutions = 0;
        c = 0;
        cin >> a >> b;
        //cout << a << " " << b;
        int answers[b];
        int values[(int)pow(2,a-2)][a-2];
        
        for(d = 0; d < pow(2,a-2) ; d++) {
            for ( e = a - 3 ; e >= 0 ; e--) {
                if (d&(int)pow(2,e)) {
                    values[d][e] = 1;
                } else {
                    values[d][e] = 0;
                }
            }
           // for ( e = a - 3 ; e >= 0 ; e--) {
             //cout << values[d][e];
            //}
            //cout <<endl;
            isPrime = false;
            for (f = 2 ; f <= 10 ; f++) {
                tmp = 0;
                tmp = pow(f,0) + pow(f,a-1);
                //cout << "tmp f " << f << " " << tmp << endl;
                for ( e = a - 3 ; e >= 0 ; e--) {
                    //cout << pow(f,e+1) << " " <<values[d][e] << endl;
                    tmp += pow(f,e+1)*values[d][e];
                }
                //cout << "tmp f " << tmp << endl;
                dividors[f-2] = isItPrime(tmp);
                //cout << dividors[f-2] << " ";
                if (dividors[f-2] < 0) {
                    isPrime = true;
                   // cout << "isPrime" << "because of" << tmp  << " base " << f << endl;
                    break;
                }
            }
            if (isPrime) {
                continue;
            } else {
                cout << 1;
                for ( e = a - 3 ; e >= 0 ; e--) {
                    cout << values[d][e];
                }
                cout << 1 << " ";
                for (z = 0 ; z < 9; z++) {
                    cout << dividors[z] << " ";
                }
                nbSolutions++;
            }
            if (nbSolutions == b) {
                break;
            }
            cout << endl;
        }
        cout << endl;
        
    }
    
    return 0;
}