/*
ID: Tariqul
PROG:
LANG: C++
*/

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
//typedef long long Long;
typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; }
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; }
bool readd(double &n){ return scanf("%lf",&n) == 1; }
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

template<class T>
T gcd(T a,T b) { if(a < b)return gcd(b,a); if(b==0)return a; return gcd(b,a%b); }

string s[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char id[10];
int cnt[150];
void init()
{
    int i,j,ki,kj;
    bool found;
    fo(i,0,10)
    {
        id[i] = '*';
        foo(ki,0,s[i])
        {
            found = false;
            fo(j,0,10)if(i != j)foo(kj,0,s[j])
            {
                if(s[i][ki] == s[j][kj]){ found = true; break; }
            }
            if(false == found){ id[i] = s[i][ki]; break; }
        }
    }
    fo(i,0,10)
    {
        if(i % 2 == 0)continue;
        foo(ki,0,s[i])
        {
            found = false;
            fo(j,0,10)if(i != j)if(j % 2 == 1)foo(kj,0,s[j])
            {
                if(s[i][ki] == s[j][kj]){ found = true; break; }

            }
            if(false == found){ id[i] = s[i][ki]; break; }
        }
    }
    id[9] = 'E';
    //fo(i,0,10)cout << i << " == " << id[i] << endl;

}
string si,ans;

void update(string &ss)
{
    int i;
    foo(i,0,ss)cnt[ss[i]]--;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	init();
	//return 0;
	int Case,t,i,j,n;
	char ch,tmp;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{
		printf("Case #%d: ",Case);
        cin >> si; CLR(cnt,0);
        foo(i,0,si)cnt[si[i]]++;
        ans = "";
        for(i = 0; i < 10; i += 2)
        {
            ch = id[i]; tmp = i + '0';
            n = cnt[ch];
            fo(j,0,n)
            {
                update(s[i]);
                ans += tmp;
            }
        }
        for(i = 1; i < 9; i += 2)
        {
            ch = id[i]; tmp = i + '0';
            n = cnt[ch];
            fo(j,0,n)
            {
                update(s[i]);
                ans += tmp;
            }
        }
        for(i = 9; i < 10; i += 2)
        {
            ch = id[i]; tmp = i + '0';
            n = cnt[ch];
            fo(j,0,n)
            {
                update(s[i]);
                ans += tmp;
            }
        }
        sort(li(ans));
        cout << ans;
		cout << endl;
	}
	return 0;
}

