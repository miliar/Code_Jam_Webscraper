// Version 2.62
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
#define vs vector<string>
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
    string scanln() { string t = ""; while(t.size()==0) getline(cin,t); return t; }
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
vi getVector(int size) { vi toRet(size); forn(i,size) toRet[i] = getInt(); return toRet; }

template<class t> void setArray(t* arr,int size,t v) { forn(i,size) arr[i] = v;}
template<class t> t* carray(int N) { return (t*)calloc(sizeof(t),N); }
template<class t> t** carray(int N,int M) { t** toRet = (t**)calloc(sizeof(t*),N); forn(i,N) toRet[i] = (t*)calloc(sizeof(t),M); return toRet; }
template<class t> void freeMatr(t** matr,int N,int M) { forn(i,N) free(matr[i]); free(matr); }

template<class t> void sortUp(t* arr,int n) { sort(arr,&arr[n]); }
template<class t> void sortUp(vector<t> &V) { sort(all(V)); }
template<class t> void sortDown(t* arr,int n) { sort(arr,&arr[n],greater<t>()); }
template<class t> void sortDown(vector<t> &V) { sort(all(V),greater<t>()); }

template<class t> vector<t> subvector(vector<t> &V,int st,int len) { return vector<t>(V.begin()+st,V.begin()+st+len); }
template<class t> void append(vector<t> &V,vector<t> &S) { V.insert(V.end(),S.begin(),S.end()); }
template<class t> void operator+=(vector<t>& V,t i) { V.push_back(i); }
template<class t> void operator+=(vector<t>& V,vector<t>& a) { append(V,a); }
template<class t> void operator-=(vector<t>& V,t ind) { V.erase(V.begin()+ind); }

vs split(const string &s, char delim) { vs elems; stringstream ss(s); string item; while(getline(ss,item,delim)) elems+=(item); return elems; }

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
vi primeList(int n) { vi T; bool* A = carray<bool>(n+1); forr(i,2,n+1) {if(!A[i]) {T.push_back(i); for(int j = i*2;j<=n;j+=i) A[j] = true;}} free(A); return T;}

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

void solve()
{
    /// START HERE <-----------------------------------------
    int n = getInt();
    int k = getInt();
    int arr[n-k+1];
    //printf("%d %d\n",n,k);
    forn(i,n-k+1) {
        scan >> arr[i];
        //printf("%d ",arr[i]);
    }
    vi V[k];
    int now = 0;
    for(int i = 1;i < n-k+1;i++) {
        int diff = arr[i]-arr[i-1];
        V[now++] += diff;
        now %= k;
    }
    int armLen[k];
    int maxArmLen = 0;
    int targSum = arr[0];
    for(int i = 0;i < k;i++) {
        // let's travel !
        int minD = 0;
        int maxD = 0;
        int nowD = 0;
        for(int j = 0;j < V[i].size();j++)
        {
            nowD += V[i][j];
            minD = min(nowD,minD);
            maxD = max(nowD,maxD);
        }
        minD = abs(minD);
        armLen[i] = minD+maxD;
        maxArmLen = max(armLen[i],maxArmLen);
        targSum -= minD;
    }
    int ans = maxArmLen;
    int neededSum;
    if(targSum >= 0) neededSum = targSum - (targSum/k*k);
    else neededSum = targSum + (((abs(targSum)%k)==0?0:1) + abs(targSum)/k)*k;
    //printf("%d -> %d\n",targSum,neededSum);
    for(int i = 0;i < k;i++) {
        neededSum -= maxArmLen-armLen[i];
    }
    if(neededSum > 0) {
        ans++;
        // ans +1 , needSum -= k-1
        //ans += neededSum/(k-1) + ((neededSum%(k-1)==0)?0:1);
        //ans += neededSum/k + ((neededSum%k==0)?0:1);
    }
    printf("%d\n",ans);
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
