/* *********************************************************************
   *                       Problem: --------------                     *
   *                   Runtime: 0.000 sec; Rank: 0000                  *
   *                     Algo Used: ----------------                   *
   *                    Solved By : Niloy - JU-CSE-21                  *
   ********************************************************************* */
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <list>
#include <iterator>
/* ********************
   *     Defines      *
   ******************** */
#define max(a,b) ((a>b)?a:b)                        //finding max
#define min(a,b) ((a<b)?a:b)                        //finding min
#define Max(a,b,c) max(a,max(b,c))                  //finding max between 3 numbers
#define Min(a,b,c) min(a,min(b,c))                  //finding min between 3 numbers
#define FOR(i,s,e) for(i=s;i<=e;i++)                //for loop with 1 increment
#define For(i,s,e,d) for(i=s;i<=e;i+=d)             //for loop with manual increment
#define _For(i,s,e,d) for(i=s;i>=e;i-=d)             //for loop with manual increment
#define Pi acos(-1.0)                               //defining Pi for mathematical uses
#define Clear(a) memset(a,0,sizeof(a))              //clearing memory of an array
#define setfalse(a) memset(a,false,sizeof(a))       //setting the array into false
#define settrue(a) memset(a,true,sizeof(a))         //setting the array into true
#define clrstr(a) memset(a,'\0',sizeof(a))          //setting string array to null
#define open freopen("C-small-attempt0.in","r",stdin)         //opening input file
#define close freopen ("output.txt","w",stdout)     //opening output file
#define Case(a) printf("Case %d: ",a)               //printing case number
#define caseh(a) printf("Case #%d: ",a)             //printing case number having '#'
#define getcase(a) scanf("%d",&a)                   //scanning case number
#define S1(a) scanf("%d",&a)                        //scan one int
#define S2(a,b) scanf("%d%d",&a,&b)                 //scan two int
#define S3(a,b,c) scanf("%d%d%d",&a,&b,&c)          //scan three int
#define SL1(a) scanf("%lld",&a)                     //scanf one long long
#define SL2(a,b) scanf("%lld%lld",&a,&b)            //scanf two long long
#define SL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)   //scanf two long long
#define CHR getchar()                               //avoid the newline character problem
#define caseloop(a,b) for(a=1;a<=b;a++)             //making case loop
#define EPS 1e-9                                    //small value for avoiding preccesion error
#define LL long long                                //long long short form
#define ULL unsigned long long                      //unsigned long long sort form
#define MX 10500                                    //MAX size/value
#define PB(x) push_back(x)                          //push in vector/string
#define PP pop_back()                               //pop from vector
#define PF(x) push_front(x)                         //push in vector/string/deque from front
#define PPF(x) pop_front()                          //pop from vector/deque from front
#define IN(x) insert(x)                             //insert element in set
#define PS(x) push(x)                               //push element in stack/queue
#define P() pop()                                   //pop element from stack/queue
#define SZ() size()                                 //return size
#define MOD 1000000007                              //mod value
#define INF (1<<28)                                 //infinity value
#define Y 1                                         //true value
#define N 0                                         //false value

using namespace std;

template <typename T> T BigMod (T b,T p,T m) {if (p == 0) return 1; if (p%2 == 0){T s = BigMod(b,p/2,m); return ((s%m)*(s%m))%m;} return ((b%m)*(BigMod(b,p-1,m)%m))%m;}
template <typename T> T ModInv (T b,T m) {return BigMod(b,m-2,m); }
template <typename T> void ia (T a[],int n) { for (int i=0;i<n;i++) cin >> a[i];}
template <typename T> void pa (T a[],int n) { for (int i=0;i<n-1;i++) cout << a[i] << " "; cout << a[n-1] << endl;}
template <typename T> T gcd(T a,T b) { if (!b) return a; return gcd(b,a%b); }
template <typename T> T POW(T b,T p) { if (p == 0) return 1; if (p%2 == 0) { T s = POW(b,p/2); return s*s; } return b*POW(b,p-1); }

LL a []= {1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004};

string i2s(LL n)
{
    string ans = "";

    while (n)
    {
        ans += n%10+'0';

        n /= 10;
    }

    return ans;
}

bool isPal(string A)
{
    for (int i=0,j=A.length()-1;i<=j;i++,j--)
    {
        if (A[i]!=A[j])
            return false;
    }

    return true;
}

//void pre_cal()
//{
//    for (LL i=1;i<=10000000;i++)
//    {
//        if (isPal(i2s(i)) && isPal(i2s(i*i)))
//        {
//            cout << i*i << endl;
//            a.PB(i*i);
//        }
//    }
//}

int B_Search(int n,int m)
{
    int l = 0,h = 38,mid;

    while (l<=h)
    {
        mid = (l+h)>>1;

        if (a[mid]<n)
        {
            l = mid+1;
        }

        else h = mid-1;
    }

    int lw = l;

    l = 0; h = 38;

    while (l<=h)
    {
        mid = (l+h)>>1;

        if (a[mid]>m)
        {
            h = mid-1;
        }

        else l = mid+1;
    }

    int hg = h;

    return hg-lw+1;
}

int main ()
{
    int t,c;

    open;close;

    getcase(t);
    caseloop(c,t)
    {
        int n,m;
        cin >> n >> m;

        caseh(c);

        cout << B_Search(n,m) << endl;
    }

    return 0;
}
