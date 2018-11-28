/*
 Some famous quotes about the greatest batsman on earth =>  <--------------SACHIN TENDULKAR------------------->
 "I want my son to become Sachin Tendulkar."-Brian Lara(WI)
 "We did not lose to a team called India, we lost to a man called Sachin."-Mark Taylor(AUS)
 "There are 2 kinds of batsmen in this world. 1)Sachin Tendulkar 2)All of the others."-Andy Flower(ZIM)
 "I have seen God. He bats at no.4 for India in tests."-Matthew Hayden(AUS)
 "I see myself when i see Sachin batting."-Don Bradman(AUS)
 "Commit you sins while Sachin is batting, for even the lord is watching"-(AUS fan)
 "Sachin is a genius , i am a mere mortal!"-Brian Lara(WI)
 "I would go to bed having nightemares of sachin dancing down the ground and hitting me for sixes."-Shane Warne(AUS)
 "Don't bowl him bad balls, he hits the good ones for fours."-Michael Kasprowicz(AUS)
 "Nothing bad can happen to us if we're on a plane in India with Sachin Tendulkar on it.(After terror attacks)"-Hashim Amla(RSA)
 "I never get tired during umpiring whenever sachin is on crease"-Rudi Kortzen(umpire)
 "Sachin Tendulkar! If he isn't the best player in the world, I want to see the best player in the world".-David Shepard(umpire)
 "If cricket is religion, Sachin is god"-(all fans)
 */

// <-------TEMPLATE--------->
// Author: suh_ash2008
#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <limits.h>
#include <string.h>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x))
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for(__typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF 100000000000000000LL
#define EPS (double)1e-6
#define is istringstream
#define os ostringstream
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair< int,int > ii;
typedef pair< int,ii > pii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef set< int > si;
typedef vector< vi > vvi;
/*
 // <----------------------FAST I/O---------------------->
 #define MAXX 4000000
 char *ipos,*opos,InpFile[MAXX],OutFile[MAXX],DIP[30];
 inline int input_int(int flag=0){while(*ipos<=32)++ipos;if(flag)return(*ipos++-'0');int x=0,neg=0;char c;while(true){c=*ipos++;if(c=='-')neg=1;else{if(c<=32)return neg?-x:x;x=(x<<1)+(x<<3)+c-'0';}}}
 inline LL input_LL(int flag=0){while(*ipos<=32)++ipos;if(flag)return(*ipos++-'0');LL x=0,neg=0;char c;while(true){c=*ipos++;if(c=='-')neg=1;else{if(c<=32)return neg?-x:x;x=(x<<1)+(x<<3)+c-'0';}}}
 inline void input_st(char *s){while(*ipos<=32)++ipos;int pos=0;char c;while(true){c=*ipos++;if(c<=32){s[pos]='\0';break;}else s[pos++]=c;}}
 inline char input_ch(){while(*ipos<=32)++ipos;char c=*ipos++;return c;}
 inline void output(int x){int y;int dig=0;while(x||!dig){y=x/10;DIP[dig++]=x-((y<<3)+(y<<1))+'0';x=y;}while(dig--)*opos++=DIP[dig];}
 inline void InitFASTIO(){ipos=InpFile;opos=OutFile;fread_unlocked(InpFile,MAXX,1,stdin);}
 inline void FlushFASTIO(){fwrite_unlocked(OutFile,opos-OutFile,1,stdout);}
 // <----------------------END OF FAST I/O---------------------->
 */
// <----------------------END OF TEMPLATE---------------------->

// <---------------------MAIN CODE STARTS HERE--------------------->

int n = 15;
LL maxV = 1000000000000000000LL;
LL valid[] = {1, 4, 9, 121, 484, 12321, 14641, 44944, 1234321, 123454321, 125686521, 12345654321, 1234567654321, 123456787654321, 12345678987654321};

LL get(string s) {
    is sin(s);
    LL v;
    sin >> v;
    return v;
}

int main(){
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");
    int t, kase = 0;
    fin >> t;
    while(t--) {
        kase++;
        fout << "Case #" << kase << ": ";
        string A, B;
        fin >> A >> B;
        LL a, b;
        if(sz(A) > 17)  fout << "0\n";
        else{
            a = get(A);
            if(sz(B) > 17)  b = maxV;
            else b = get(B);
            int ans = 0;
            REP(i, n)   if(valid[i] >= a && valid[i] <= b)  ans++;
            fout << ans << "\n";
        }
    }
    fin.close();
    fout.close();
}
