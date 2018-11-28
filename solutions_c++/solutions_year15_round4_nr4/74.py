// Version 2.6
#define TESTCASE true
#define DEBUG false
#define GCJ_TESTCASE true

#include <bits/stdc++.h>
#include <math.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define forn(s,t) for(int s = 0;s < t;s++)
#define forr(i,s,e) for(int i = s;i < e;i++)
#define forn1(s,t) for(int s = 1;s <= t;s++)

#define gcd(a,b) __gcd(a,b) // GNU GCC only !

#define MIN_HEAP true
#define MAX_HEAP false

#define pii pair<int,int>
#define vi vector<int>
#define v vector
#define all(v) v.begin(),v.end()
#define gint(a) int a = getInt();

typedef long long int lli;
typedef unsigned long long int ulli;
using namespace std;

void printArray(int* arr,int n) { forn(i,n) printf("%d ",arr[i]);}
void printVector(vi &V) { forn(i,V.size()) printf("%d ",V[i]); }

class scanner { public :
    scanner& operator >>(int& t) { scanf("%d",&t); return *this; };
    scanner& operator >>(double& t) { scanf("%lf",&t); return *this; };
    scanner& operator >>(string& t) { scanf("%s",buf); t=buf; return *this; };
    scanner& operator >>(lli& t) { scanf("%lld",&t); return *this; };
    scanner& operator >>(char& t) { scanf("%s",buf); t=buf[0]; return *this; };
    string scanln() { string t; getline(cin,t); return t; }
    char buf[10000];
} scan;
class outputter { public :
    outputter& operator <<(int t) { printf("%d",t); return *this; }
    outputter& operator <<(double t) { printf("%lf",t); return *this; };
    outputter& operator <<(string t) { printf("%s",t.c_str()); return *this; };
    outputter& operator <<(lli t) { printf("%lld",t); return *this; };
    outputter& operator <<(vi V) { printVector(V); return *this;}
} print;

int getInt() { int a; scanf("%d",&a); return a; }
void getInt(int& a) { scanf("%d",&a); }
void getInt(int& a,int &b) { scanf("%d %d",&a,&b); }
double getDouble() { double a; scanf("%lf",&a);return a; }
void getDouble(double& a) { scanf("%lf",&a); }
void getArray(int *arr,int size) { forn(i,size) getInt(arr[i]); }
void getArray(int **arr,int N,int M) { forn(i,N) forn(j,M) getInt(arr[i][j]);}
void getArray(double *arr,int size) { forn(i,size) getDouble(arr[i]); }
void getArray(double **arr,int N,int M) { forn(i,N) forn(j,M) getDouble(arr[i][j]); }
template<class t> void setArray(t* arr,int size,t v) { forn(i,size) arr[i] = v;}
vi getVector(int size) { vi toRet(size); forn(i,size) toRet[i] = getInt(); return toRet; }
template<class t> void sortUp(t* arr,int n) { sort(arr,&arr[n]); }
template<class t> void sortUp(vector<t> &V) { sort(all(V)); }
template<class t> void sortDown(t* arr,int n) { sort(arr,&arr[n],greater<t>()); }
template<class t> void sortDown(vector<t> &V) { sort(all(V),greater<t>()); }
template<class t> t* array(int N) { return (t*)calloc(sizeof(t),N); }
template<class t> t** array(int N,int M) { t** toRet = (t**)calloc(sizeof(t*),N); forn(i,N) toRet[i] = (t*)calloc(sizeof(t),M); return toRet; }
template<class t> void freeMatr(t** matr,int N,int M) { forn(i,N) free(matr[i]); free(matr); }
template<class t> vector<t> subvector(vector<t> &V,int st,int len) { return vector<t>(V.begin()+st,V.begin()+st+len); }
template<class t> void append(vector<t> &V,vector<t> &S) { V.insert(V.end(),S.begin(),S.end()); }
inline bool validPos(int x,int y,int w,int h) { return !(x<0||y<0||x>=w||y>=h); }

ulli fac(int n) { ulli toRet = 1; forr(i,2,n+1) toRet *= i; return toRet; }
lli gcdSlow(lli a,lli b) { if(a>=b) { if(a%b) return gcdSlow(b,a%b); return b; } else { if(b%a) return gcdSlow(a,b%a); return a; }} /// [SLOW] use __gcd (gcc only)
inline lli lcmSlow(lli a,lli b) { return a*b/gcdSlow(a,b); } /// [SLOW] use lcm (gcc only)
inline lli lcm(lli a,lli b) { return a*b/gcd(a,b); }
ulli C(int n,int r) {  ulli t = 1; for(int i = r+1;i <= n;i++) t *= i; for(int i = 2;i <= n-r;i++) t/= i; return t; } /// n!/r!(n-r)!
ulli P(int n,int r) { ulli t = 1; for(int i = n-r+1;i <= n;i++) t *= i; return t; } /// n!/(n-r)!
lli pow10(int n) { lli toRet = 1; forn(i,n) toRet*=10; return toRet; }
lli pow(int b,int e) { lli toRet = 1; forn(i,e) toRet*=b; return toRet; }
int getDig(lli num,int d) { return (num/pow10(d))%10; }
bool deq(double a,double b) { return fabs(a-b)<=0.0000000001; } /// 1*10^-10
vi primeList(int n) { vi T; bool* A = array<bool>(n+1); forr(i,2,n+1) {if(!A[i]) {T.push_back(i); for(int j = i*2;j<=n;j+=i) A[j] = true;}} free(A); return T;}

template<class t> void operator+=(vector<t>& V,t i) { V.push_back(i); }
template<class t> void operator+=(vector<t>& V,vector<t>& a) { append(V,a); }
template<class t> void operator-=(vector<t>& V,t ind) { V.erase(V.begin()+ind); }

template<class t> class heap { public :
    heap(bool a) { minHeap = !a; } /// true = minHeap , false = maxHeap
    void push(t data) { V.push_back(data); if(minHeap) push_heap(all(V)); else push_heap(all(V),greater<t>()); }
    void operator+=(t data) { push(data); }
    void operator+=(heap& oth) { forn(i,oth.V.size()) push(oth.V[i]);}
    t operator[](int ind) { return V[ind];}
    bool empty() { return V.size()==0;}
    t pop() { t toRet = V[0]; if(minHeap) pop_heap(all(V)); else pop_heap(all(V),greater<t>()); V.pop_back(); return toRet; }
    bool minHeap;
    v<t> V;
};
vector<string> pass;
int place(int **arr,int r,int c,int x,int y) {
    if(y==r) {
        // checking
        forn(i,r) {
            forn(j,c) {
                int cnt = 0;
                if(arr[i][(j+1) % c] == arr[i][j]) cnt++;
                if(arr[i][(j==0)?(c-1):(j-1)] == arr[i][j]) cnt++;
                if(i<r-1 && arr[i+1][j] == arr[i][j]) cnt++;
                if(i>0 && arr[i-1][j] == arr[i][j]) cnt++;
                if(cnt != arr[i][j]) {
                    return 0;
                }
            }
        }
        /*forn(i,r) {
            forn(j,c) {
                printf("%d",arr[i][j]);
            }
            printf("\n");
        }
        printf("\n");*/

        // check with before
        string str;
        forn(R,c) { // rotate
            str = "";
            forn(i,r) {
                forn(j,c) {
                    str.push_back('0'+arr[i][(j+R)%c]);
                }
            }
            forn(i,pass.size()) {
                if(pass[i] == str) return 0;
            }
        }
        pass.push_back(str);
        return 1;
    }
    int toRet = 0;
    for(int i = 1;i <= 3;i++) {
        arr[y][x] = i;
        if(i==1) {
            //if(y>0 && x>0 && arr[y-1][x] == 1 && arr[y][x-1] == 1) continue;
        }
        if(x==c-1) {
            if(y>=1) {
                // check 2 row above
                bool pass = true;
                forn(j,c) {
                    int cnt = 0;
                    if(arr[y-1][(j+1) % c] == arr[y-1][j]) cnt++;
                    if(arr[y-1][(j==0)?(c-1):(j-1)] == arr[y-1][j]) cnt++;
                    if(y-1<r-1 && arr[y][j] == arr[y-1][j]) cnt++;
                    if(y-1>0 && arr[y-2][j] == arr[y-1][j]) cnt++;
                    if(cnt != arr[y-1][j]) {
                        pass = false;
                        break;
                    }
                }
                if(!pass) continue;
            }
            toRet += place(arr,r,c,0,y+1);
        }
        else {
            toRet += place(arr,r,c,x+1,y);
        }
    }
    return toRet;
}
void solve()
{
    /// START HERE <-----------------------------------------
    int r,c;
    scan >> r >> c;
    int **arr = array<int>(r,c);
    printf("%d\n",place(arr,r,c,0,0));
    freeMatr(arr,r,c);
    /*if(r==2) ans = 1;
    if(r==3) {
        if(c==2) ans = 2;
        if(c==3) ans = 2;
        if(c==4) ans = 3;
        if(c==5) ans = 2;
        if(c==6) ans = 2;
    }
    if(r==4) {
        if(c==2) ans = 1;
        if(c==3) ans = 1;
        if(c==4) ans = 1;
        if(c==5) ans = 1;
        if(c==6) ans = 1;
    }
    if(r==5) {
        if(c==2) ans = 1;
        if(c==3) ans = 1;
        if(c==4) ans = 2;
        if(c==5) ans = 1;
        if(c==6) ans = 1;
    }
    if(r==6) {
        if(c==2) ans = 2;
        if(c==3) ans = 2;
        if(c==4) ans = 2;
        if(c==5) ans = 2;
        if(c==6) ans = 2;
    }*/
}

int main()
{
    if(TESTCASE) {
        int t,tt;
        scanf("%d",&tt);
        for(t=0;t < tt;t++)
        {
            if(GCJ_TESTCASE) printf("Case #%d: ",t+1);
            solve();
        }
    } else {
        solve();
    }
}
