#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <math.h>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const double pi=acos(-1.0);
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
typedef map<string, int> simp;
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
#define Sort(v) sort((v).begin(), (v).end())
#define Uni(v) Sort(v),(v).erase(unique((v).begin(), (v).end()), (v).end())
#define cl(a,b) memset(a,b,sizeof(a))

const int oo=1000000;

#pragma warning(disable:4996)

#define QX "C"

int N;
int nm[32];
ull pw2[32][11];
ull pw3[32][11];
ull pw5[32][11];
ull pw7[32][11];
ull pw11[32][11];

// return 0 if it's prime
ull get_nontrivial_divisor(ll n)
{
    //ull m = (ull) sqrt((double)n) + 1;
    //if (m>=n) m = n - 1;
    ull m = 7;
    for (ull i = 2; i <= m; i++){
      if (n % i == 0) {
        return i;
      }
    }
    return 0;
}

ull get_nontrivial_divisor(int N, int base)
{
    /*cout<<N<<","<<base<<"-";
    rep(i,N) {
        cout<<nm[i];
    }
    cout<<endl;*/

    ull n = 0;
    rep(i,N) {
        n += pw2[i][base] * nm[i];
    }
//    cout<<"n2="<<n<<endl;
    if (n % 2 == 0) {
        //cout<<n<<" "<<base<<" "<<nm[0]<<" "<<pw2[0][base]<<endl;
        return 2LL;
    }

    n = 0;
    rep(i,N) {
        n += pw3[i][base] * nm[i];
    }
//    cout<<"n3="<<n<<endl;
    if (n % 3 == 0) {
        return 3LL;
    }

    n = 0;
    rep(i,N) {
        n += pw5[i][base] * nm[i];
    }
//    cout<<"n5="<<n<<endl;
    if (n % 5 == 0) {
        return 5LL;
    }

    n = 0;
    rep(i,N) {
        n += pw7[i][base] * nm[i];
    }
//    cout<<"n7="<<n<<endl;
    if (n % 7 == 0) {
        return 7LL;
    }

    n = 0;
    rep(i,N) {
        n += pw11[i][base] * nm[i];
    }
    if (n % 11 == 0) {
        return 11LL;
    }

    return 0;
}

int main()
{
//	freopen("../" QX ".txt","r",stdin);
//	freopen("../" QX "-small-attempt0.in","r",stdin);freopen("../" QX "-small-attempt0.out","w",stdout);
//	freopen("../" QX "-small-attempt1.in","r",stdin);freopen("../" QX "-small-attempt1.out","w",stdout);
	freopen("../" QX "-large.in","r",stdin);freopen("../" QX "-large.out","w",stdout);

    For(b,2,11) {
        pw2[0][b] = 1;
        pw3[0][b] = 1;
        pw5[0][b] = 1;
        pw7[0][b] = 1;
        pw11[0][b] = 1;
        For(i,1,32) {
            pw2[i][b] = (pw2[i-1][b] * b) % 2;
            pw3[i][b] = (pw3[i-1][b] * b) % 3;
            pw5[i][b] = (pw5[i-1][b] * b) % 5;
            pw7[i][b] = (pw7[i-1][b] * b) % 7;
            pw11[i][b] = (pw11[i-1][b] * b) % 11;
        }
        /*cout<<"2-"<<b<<"-";
        For(i,0,N) {
            cout<<pw2[i][b];
        }
        cout<<endl;
        cout<<"3-"<<b<<"-";
        For(i,0,N) {
            cout<<pw3[i][b];
        }
        cout<<endl;
        cout<<"5-"<<b<<"-";
        For(i,0,N) {
            cout<<pw5[i][b];
        }
        cout<<endl;
        cout<<"7-"<<b<<"-";
        For(i,0,N) {
            cout<<pw7[i][b];
        }
        cout<<endl;
        cout<<"11-"<<b<<"-";
        For(i,0,N) {
            cout<<pw11[i][b];
        }
        cout<<endl;*/
    }

    int T=0;
	scanf("%d",&T);
    for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        int N, J;
        cin>>N>>J;
        cout << "Case #" << caseId << ":" << endl;

        int j = 0;

        memset(nm,0,sizeof(nm));
        nm[N-1] = 1;
        nm[1] = -1;
        nm[0] = 1;
        while(j < J) {
            nm[1]++;
            int i = 1;
            while(nm[i] == 2) {
                nm[i] = 0;
                nm[++i]++;
            }
            ull divisors[11] = {0};
            bool succ = true;
            for (int b = 10; b >= 2; b--) {
                ull divisor = get_nontrivial_divisor(N, b);
                if (!divisor) {
                    succ = false;
                    break;
                }
                divisors[b] = divisor;
            }
            if (succ) {
                rep(i,N) {
                    cout<<nm[N-i-1];
                }
                For(b,2,11) {
                    cout<<" "<<divisors[b];
                }
                cout<<endl;
                j++;
                // debug
                /*For(b,2,11) {
                    ull n = 0;
                    rep(i,N) {
                        n += pw[i][b] * nm[i];
                    }
                    cout<<b<<":"<<n<<"->"<<divisors[b]<<"->" <<n % divisors[b]<<endl;
                }
                cout<<endl;*/

            }
        }
	}
    return 0;
}
