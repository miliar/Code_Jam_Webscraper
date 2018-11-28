#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;


const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
#define PI 3.1415926535897932384626

#define    READ(f) 	         freopen(f, "r", stdin)
#define    WRITE(f)   	     freopen(f, "w", stdout)
//
//#define    vi 	 vector < int >
//#define    vii 	 vector < vector < int > >

typedef pair <int,int>pii;

#define ff first
#define ss second

//******************DELETE****************
#define arnab
#ifdef arnab
     #define debug(args...) {dbg,args; cerr<<endl;}
#else
    #define debug(args...)  // Just strip off all debug tokens
#endif

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;
//******************DELETE****************

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T _swap(T &a, T &b) { a=a^b;b=a^b;a=a^b;}
template< class T > T gcd(T a, T b) { return (b == 0 ? a : gcd(b, a % b)); }
template< class T > T lcm(T a, T b) { return (a / gcd(a, b) * b); }

typedef pair<int,int>ii;
typedef vector<ii>vii;
typedef vector<int>vi;




int main()
{
        READ("in.txt");
    WRITE("out.txt");
    int T,i;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        int x,r,c;
        scanf("%d %d %d", &x,&r,&c);
        //cout<< x << " "<<  r << " "<< c<<endl;
        printf("Case #%d: ",i);
        int f;
        int t1=min(r,c);
        int t2=max(r,c);
        //t1--;
        if((r*c)%x!=0)
        {
            printf("RICHARD\n");
        }

        else if(t2<x)
        {
            printf("RICHARD\n");
        }

        else if(t1+1<x)
        {
            printf("RICHARD\n");
        }
        else
        {
            printf("GABRIEL\n");
        }
    }
    return 0;
}


//10
//8 1 9 8 3 4 6 1 5 2



