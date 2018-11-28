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
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
 
using namespace std;
 
typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
 
const int maxn=10000+16;
int main()
{	int t,x,l,r;
cin>>t;
for(int i=1;i<=t;i++){
	
	cin>>x>>l>>r;
	int cc=1;
            if( x>=7 || r*l<x || (l*r)%x!=0 ){}
            else if(x==2 && l>1 && r>1)cc=0;
            else if(r>x-1 && l>x-2)cc=0;
            else if(r>x-2 && l>x-1)cc=0;
            if(cc!=0) cout<<"Case #"<<i<<": RICHARD"<<endl;
            else cout<<"Case #"<<i<<": GABRIEL"<<endl;
}
	}