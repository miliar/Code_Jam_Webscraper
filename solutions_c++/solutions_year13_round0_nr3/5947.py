/*
http://codingaquarium.wordpress.com/
Shaikh shiam Rahman

*/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <iomanip>

using namespace std;

/*** typedef ***/

#define MEMSET_INF 127
#define MEMSET_HALF_INF 63
#define stream istringstream
#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define repl(i,n) for(__typeof(n) i=1; i<=(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define INF (1<<30)
#define PI acos(-1.0)
#define pb push_back
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x))
#define memsp(x) mem(x,MEMSET_INF)
#define memdp(x) mem(x,-1)
#define memca(x) mem(x,0)
#define eps 1e-9
#define pii pair<int,int>
#define pmp make_pair
#define ft first
#define sd second
#define vi vector<int>
#define vpii vector<pii>
#define si set<int>
#define msi map<string , int >
#define mis map<int , string >
typedef long long i64;
typedef unsigned long long ui64;

/** function **/

#define SDi(x) sf("%d",&x)
#define SDl(x) sf("%lld",&x)
#define SDs(x) sf("%s",x)
#define SD2(x,y) sf("%d%d",&x,&y)
#define SD3(x,y,z) sf("%d%d%d",&x,&y,&z)
#define pf printf
#define sf scanf
#define ll long long

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

string itoa(long long a){if(a==0) return "0";string ret;for(long long i=a; i>0; i=i/10) ret.push_back((i%10)+48);reverse(ret.begin(),ret.end());return ret;}

bool palindrome(string word) {
    int i = 0, j = word.length()- 1;
    while (i < j) {
        if (word.at(i++) != word.at(j--)) {
            return false;
        }
    }
    return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	READ("in.txt");
	WRITE("OUT.txt");
#endif
    int tc,cas=1;
    cin>>tc;
    while(tc--)
    {
        pf("Case #%d: ",cas++);
        int A,B;
        SD2(A,B);
        int rA = ceil(sqrt(A)),rB = floor(sqrt(B)),counter  = 0;
        FOR(i,rA,rB){
            if(palindrome( itoa((ll)i) )){
                if(palindrome( itoa((ll)i*i) ))
                    counter++;
            }
        }
        pf("%d\n",counter);
    }
    return 0;
}
