//{ Template
using namespace std;
//{ C-headers
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cctype>
#include <cassert>
#include <ctime>
//}
//{ C++-headers
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS 1e-7
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2*acos (0.0)
//}
typedef long long int64;
typedef unsigned long long int64u;
#define memo(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define db double
#define pb push_back
#define pii pair<int ,int >
#define NL puts("")
//{
//Intput_Output
#define II ({ int a; scanf("%d",&a); a;})
#define IL ({ int64 a; scanf("%lld",&a);  a;})
#define ID ({ db a; scanf("%lf",&a);  a;})
#define IC ({ char a; scanf("%c",&a);  a;})
#define IS ({ string a; cin >> a;  a;})
#define ICA(n) ({ char a[n]; scanf("%s",&a);  a;})
#define OC printf("Case #%d: ",cs);
//}
//}
template <class T, class U> inline T max (T &a, U &b) {
    return a > b ? a : b;
}
template <class T, class U> inline T min (T &a, U &b) {
    return a < b ? a : b;
}
template <class T, class U> inline T swap (T &a, U &b) {
    T tmp = a;
    a = b;
    b = tmp;
}
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
int dx[]= {1,1,0,-1,-1,-1,0,1};
int dy[]= {0,1,1,1,0,-1,-1,-1}; //8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[6]={2,1,-1,-2,-1,1};int dy[6]={0,1,1,0,-1,-1}; //Hexagonal Direction

const int64 INF = (1ll)<<50;
const int mx = 1e5 + 7;
const int mod = 1000000007 ;
const db pi = PI;
int EQ(double d) {
    if ( fabs(d) < EPS ) return 0;
    return d > EPS ? 1 : -1 ;
}

bool flag[12][12];
int tot,r,c,m,ix,iy;

bool valid(int x,int y) {
    return (x>=0 &&x<r&&y>0&&y<=c&& flag[x][y] == false);
}
int cnt ;
int vis[12][12];
void dfs(int x,int y) {
    if(vis[x][y]) return;
    cnt++;
    vis[x][y] = true;
    bool f = true;
    rep(k,8) {
        if(x+dx[k]<0 || x+dx[k]>=r || y+dy[k]<=0 || y+dy[k]>c) continue;
        if(flag[x+dx[k]][y+dy[k]]) {
            f = false;
            break;
        }
    }
    if(f){
        rep(i,8) {
            if(valid(x+dx[i],y+dy[i])) dfs(x+dx[i],y+dy[i]);
        }
    }
}

bool call(int num,int M) {
    if(M == m) {
        ix = -1,iy = -1;
        rep(i,r) {
            For(j,c) {
                if(flag[i][j]) continue;
                bool f = true;
                rep(k,8) {
                    if(i+dx[k]<0 || i+dx[k]>=r || j+dy[k]<=0 || j+dy[k]>c) continue;
                    if(flag[i+dx[k]][j+dy[k]]) {
                        f = false;
                        break;
                    }
                }
                if(f) {
                    ix = i,iy = j;
                    break;
                }
            }
        }
        if(ix != -1 && iy != -1) {
            cnt = 0;
            memo(vis,false);
            dfs(ix,iy);
            return (cnt == (tot-m));
        }
        return false;

    }
    if(num == tot) return false;
    int R = num/c - (num%c==0),C = (num%c==0)?c:num%c;
    flag[R][C] = true;
    if(call(num+1,M+1)) return true;
    flag[R][C] = false;
    if(call(num+1,M)) return true;

    return false;
}

int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t = II;
    For(cs,t) {
        memo(flag,false);
        r = II,c = II,m = II;
        tot = r*c;
        OC;
        NL;
        if(m == 0) {
            bool flag = true;
            rep(i,r) {
                rep(j,c) {
                    if(flag) printf("c");
                    else printf(".");
                    flag = false;
                }
                NL;
            }
        } else if(tot - m == 1) {
            bool flag = true;
            rep(i,r) {
                rep(j,c) {
                    if(flag) printf("c");
                    else printf("*");
                    flag = false;
                }
                NL;
            }
        } else if( r == 1 ) {
            int tmp = 0;
            For(i,c) {
                if(i == c)
                    printf("c");
                else if(tmp < m) printf("*");
                else printf(".");
                tmp++;
            }
            NL;
        } else if( c == 1) {
            int tmp = 0;
            For(i,r) {
                if(i == r)
                    printf("c");
                else if(tmp < m) printf("*");
                else printf(".");
                tmp++;
                NL;
            }
        } else if(r == 2 && c == 2) {
            printf("Impossible\n");
        } else if(r == 2) {
            if(tot - m < 4 || m%2 == 1) printf("Impossible\n");
            else {
                int tmp = 0;
                For(i,c) {
                    For(j,r) {
                        if(tmp<m)
                            flag[j][i] = true;
                        tmp++;
                    }
                }
                For(i,r) {
                    For(j,c) {
                        if(flag[i][j]) printf("*");
                        else if(i == r && j == c) printf("c");
                        else printf(".");
                    }
                    NL;
                }
            }
        } else if(c == 2) {
            if(tot - m < 4 || m%2 == 1) printf("Impossible\n");
            else {
                int tmp = 0;
                For(i,r) {
                    For(j,c) {
                        if(tmp < m) printf("*");
                        else if(i == r && j == c) printf("c");
                        else printf(".");
                        tmp++;
                    }
                    NL;
                }
            }
        }
        else if(call(1,0)) {
            //if(cs == 14) cout << ix << " " << iy << endl;
            rep(i,r) {
                For(j,c) {
                    if(flag[i][j]) printf("*");
                    else if( i == ix && j ==iy) printf("c");
                    else printf(".");
                }
                NL;
            }
        } else cout << "Impossible" << endl;

    }
}
