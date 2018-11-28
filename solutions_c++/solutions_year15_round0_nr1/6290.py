//    Author : Nishanth Vijayan IIT Ropar,India.
//
//	  Spoj 		  : http://www.spoj.com/users/nishanth_v/
//	  HackerEarth : http://www.hackerearth.com/users/nishanththegr8/
//	  Facebook	  : https://www.facebook.com/NishanthTheGr8
//    Motto       : The Less You Give A Fuck, The Happier You'll Be. :)


#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <list>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
#include <cstring>


#define ABS(x) ((x)<0?-(x):(x))
#define pnl printf("\n");
#define REP(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FOR(i,a,b) for(__typeof(b) i=(a);i<(b);++i)
#define FORE(i,a,b) for(__typeof(b) i=(a);i<=(b);++i)
#define FOREACH(i,s) for(__typeof((s).begin()) i=(s).begin();i!=(s).end();i++)
#define UNIQUE(v) sort(ALL(v)),v.erase(unique(ALL(v)),v.end())
#define FILL(a,b) memset(a,b,sizeof(a))

#define pi acos(-1)
#define INF 0x3f3f3f3f
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
#define LLI long long 
#define gc getchar_unlocked
#define pc putchar_unlocked
#define MAX 100010

using namespace std;

typedef pair<LLI, LLI> ii;
typedef vector<LLI, LLI> vi;


LLI scanint()
{register int c = gc();LLI x = 0;int neg = 0;
for(;((c<48 || c>57) && c != '-');c = gc());
if(c=='-') {neg=1;c=gc();}
for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
if(neg) x=-x;return x;}

void writeint (LLI n)
{LLI N = n, rev, count = 0;rev = N;
if (N == 0) { pc('0'); pc('\n'); return ;}
while ((rev % 10) == 0) { count++; rev /= 10;} 
rev = 0;
while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;} 
while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
while (count--) pc('0');}


int main(){

LLI T,l,cum,xtra,c;
string S;

cin>>T;
FOR(t,1,T+1){
	cin>>l;
	cin>>S;
	cum = (S[0]-'0');
	xtra = 0;
	FOR(i,1,l+1){
		c = (S[i]-'0');
		if(c>0 && (cum>=i)){cum += c;}
		else if(c>0 && (cum<i)){
			xtra += (i-cum);
			cum += (i-cum);
			cum += c;
		}
	}
	cout<<"Case #"<<t<<": "<<xtra<<endl;;


}

return 0;
}