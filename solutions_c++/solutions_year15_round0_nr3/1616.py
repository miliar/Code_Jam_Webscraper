//==================================================================
//Author        : Nguyen Trung Hieu - vuondenthanhcong11@gmail.com
//Problem Name  :
//Discription   :
//Reference from:
//==================================================================

// -------------------- include all libraries ------------------
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

using namespace std;

// -------------------- Redefine container ---------------------
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;

typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned uint;

// -------------------- Redefine some operator ------------------
#define forn(i,a,b)     for (int i=(a),_b=(b); i<_b; i++)
#define rforn(i,b,a)    for (int i=(b)-1,_a=(a); i>=_a; i--)
#define reset(a,b)      memset((a),(b),sizeof(a))
#define fi              first
#define se              second
#define pb              push_back
#define all(x)          (x).begin(),(x).end()
#define mp(x,y)         make_pair(x,x)
#define foreach(i, c)   for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define debug(x) 	    {cerr<<#x<<" = "<<x<< endl;}
#define debugArr(a,x,y)	{cerr<<#a<<" = ";forn(_,x,y) cerr << a[_] << ' '; cerr <<endl;}

// ===================== Begin template =========================
// --------------------- Quick input output ---------------------
int in(){int x=0,c;for(;(unsigned long long)((c=getchar())-'0')>= 10;){if(c=='-')return -in();if(!~c)throw~0;}do{x=(x<<3)+(x<<1)+(c-'0');}while((unsigned long long)((c=getchar())-'0')<10);return x;}
long long in64(){long long x=0,c;for(;(unsigned long long)((c=getchar())-'0')>=10;){if(c=='-')return -in();if(!~c)throw~0;}do{x=(x<<3)+(x<<1)+(c-'0');}while((unsigned long long)((c=getchar())-'0')<10);return x;}
void out(int n){char buf[33];int i=30;if(n<0)putchar('-'),n=-n;do{buf[i--]='0'+n%10;n/=10;}while(n);while(i<30)putchar(buf[++i]);}
void out64(long long n){char buf[55];int i=50;if(n<0)putchar('-'),n=-n;do{buf[i--]='0'+n%10;n/=10;}while(n);while(i<50)putchar(buf[++i]);}

void readArray(int array1[],int len){for(int i=0;i<len;i++){array1[i]=in();}}
void read2Array(int array1[],int array2[],int len){for(int i=0;i<len;i++){array1[i]=in();array2[i]=in();}}

// ===================== End template ===========================

// --------------------- Start code ------------------------------
int product(int c1,int c2){
    if(abs(c1)==1||abs(c2)==1) return c1*c2;
    int ans=1;
    if(c1*c2<0) ans=-1;
    c1=abs(c1);c2=abs(c2);
    if(c1==c2) return -ans;
    ans=ans*('i'+'j'+'k'-c1-c2);
    if(c2-c1==1||c1-c2==2) return ans;
    else return -ans;
}
int power(int c, int64 x){
    int res=1;
    while(x>0){
        if(x%2==1) res=product(res,c);
        x/=2; c=product(c,c);
    }
    return res;
}
int main() {
	freopen ("C-large.in", "r", stdin);
	freopen ("C-large.txt", "w", stdout);
	int testCase=in();
	forn(test,0,testCase){
        int64 l=in64(); int64 x=in64();
        char c[10005]; int ans=1,okI=0,okJ=0;
        forn(i,0,l){
            c[i]=getchar();
            ans=product(ans,c[i]);
        }
        if(power(ans,x)==-1){
            ans=1;
            for(int64 j=1;j<9;j++){
                for(int64 i=0;i<l;i++){
                    if(j==x&&i==l-1) break;
                    ans=product(ans,c[i]);
                    if(ans=='i'&&okI==0) okI=1;
                    if(ans=='k'&&okJ==0&&okI==1) okJ=1;
                    if(okI==1&&okJ==1) break;
                }
                if(okI==1&&okJ==1) break;
                if(j>=x) break;
            }
            if(okI==1&&okJ==1) printf("Case #%d: YES\n",test+1);
            else printf("Case #%d: NO\n",test+1);
        }
        else printf("Case #%d: NO\n",test+1);
	}
}
