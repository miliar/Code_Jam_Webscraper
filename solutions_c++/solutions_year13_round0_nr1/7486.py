#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

int pel(string s){string t;t=s;reverse(t.begin(),t.end());if(s==t)return 1;return 0;}
string toString(int n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
bool isprime(int m){if(m<2) return 0;for( int i=2; i*i<=m ; i++)if(m%i==0)return 0; return 1;return 0;}

# define eps 1e-8
# define inf (1<<30)
# define pi (2*acos(0.0))
# define __(array,w)   memset(array,w,sizeof array)
# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)
# define all(c) (c).begin(), (c).end()
# define sz(x) x.size()
# define pb push_back
# define UNQ(s) {sort(all(s));(s).erase(unique(all(s)),s.end());}
# define rive(s) reverse(s.begin(),s.end())
# define out(a) cout<<#a<<" #"<<a<<endl;
# define caout(a) cout<<#a<<" "<<++a<<": ";
# define X first
# define Y second
# define MP make_pair
typedef long long LL;
//typedef __int64   LL;
typedef vector<int>vi;
typedef vector<string>vs;
typedef pair<int,int>pri;
typedef map<string,int>msi;
typedef map<vector<int>,int>mvi;
inline bool iseq(double x,double y){if(fabs(x-y)<eps)return true;return false;}
template<typename T>inline double hpt(T x1,T y1,T x2,T y2){return hypot(x1-x2,y1-y2);}
template<typename T>inline T gcd(T a,T b){if(!b)return a;else return gcd(b,a%b);}
template<typename T>inline void extended_euclid(T a,T b,T &x,T &y){if(a%b==0)x=0,y=1;else{extended_euclid(b,a%b,x,y);T temp=x;x=y;y=-y*(a/b)+temp;}}
template<typename T>inline T bigmod(T b,T p,T m){if(!p)return 1;else if(!(p%2)){T x=bigmod(b,p/2,m);return x*x;}else return ((b%m)*bigmod(b,p-1,m))%m;}
#define PS 5
int prime[PS/32+1];
void setbit(int i){int p=i>>5,q=i&31;prime[p]|=(1<<q);}
bool checkbit(int i){int p=i>>5,q=i&31;return prime[p]&(1<<q)?true:false;}
void buildprime(int n){int i,j,k=sqrt(double(n));prime[0]=3;for(i=4;i<n;i+=2)setbit(i);for(i=3;i<=k;i+=2){if(!checkbit(i)){int ii=i+i;for(j=i*i;j<n;j+=ii)setbit(j);}}}
map<int,int>mp;

char board[4][4];
int main()
{

    #ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);
        //freopen("A-small-attempt0.in","r",stdin);

        freopen("aout.txt","w",stdout);
    #endif

    int test,Ctest=0;

    cin>>test;

    while(test--){
        REP(i,4){
            REP(j,4){
                cin>>board[i][j];
            }
        }

        int f = 0 , dot = 0;

        //checking horizontally
        REP(i,4){
            int x = 0 , t = 0 , o = 0;
            REP(j,4){
                if(board[i][j]=='.'){
                    dot++;
                }
                if(board[i][j]=='X'){
                    x++;
                }
                if(board[i][j]=='T'){
                    t++;
                }
                if(board[i][j]=='O'){
                    o++;
                }
            }
            if(x==4 || (x==3 && t==1)){
                f = 1;
            }

            if(o==4 || (o==3 && t==1)){
                f = 2;
            }
        }

        //checking vertically
        REP(i,4){
            int x = 0 , t = 0 , o = 0;
            REP(j,4){
                if(board[j][i]=='.'){
                    dot++;
                }
                if(board[j][i]=='X'){
                    x++;
                }
                if(board[j][i]=='T'){
                    t++;
                }
                if(board[j][i]=='O'){
                    o++;
                }
            }


            if(x==4 || (x==3 && t==1)){
                f = 3;
            }

            if(o==4 || (o==3 && t==1)){
                f = 4;
            }

        }

        //checking diagonally from left
        int x = 0 , t = 0 , o = 0;
        REP(i,4){
            if(board[i][i]=='.'){
                dot++;
            }
            if(board[i][i]=='X'){
                x++;
            }
            if(board[i][i]=='T'){
                t++;
            }
            if(board[i][i]=='O'){
                o++;
            }
        }
        if(x==4 || (x==3 && t==1)){
            f = 5;
        }

        if(o==4 || (o==3 && t==1)){
            f = 6;
        }

        //checking diagonally from right
        x = 0 , t = 0 , o = 0;
        for(int i = 3 ; i>=0 ; i--){

            if(board[i][3-i]=='.'){
                dot++;
            }
            if(board[i][3-i]=='X'){
                x++;
            }
            if(board[i][3-i]=='T'){
                t++;
            }
            if(board[i][3-i]=='O'){
                o++;
            }
        }

        if(x==4 || (x==3 && t==1)){
            f = 7;
        }

        if(o==4 || (o==3 && t==1)){
            f = 8;
        }

        cout<<"Case #"<<++Ctest<<": " <<((f%2==1)?"X won":((f!=0 && f%2==0)?"O won":((dot!=0)?"Game has not completed":"Draw")))<<endl;

    }




    return 0;
}
