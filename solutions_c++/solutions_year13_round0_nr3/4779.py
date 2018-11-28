#include <fstream>
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
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef long long ll;
const double pi=acos(-1.0);
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
typedef map<string, int> simp;
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
#define Sort(v) sort((v).begin(), (v).end())
#define Uni(v) Sort(v),(v).erase(unique((v).begin(), (v).end()), (v).end())
#define cl(a,b) memset(a,b,sizeof(a))

const int oo=1000000;

#pragma warning(disable:4996)

#define QX "C"

inline bool is_palindrome(ll x)
{
    if (x<10)
        return true;
    char ch[100];
    int i=0;
    while(x){
      ch[i++]=x%10;
      x/=10;
    }
    rep(j,i/2){
        if (ch[j]!=ch[i-j-1])
            return false;

    }
    return true;
}

int main()
{
//	freopen("" QX ".txt","r",stdin);
	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
//	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
//	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
    /*for(ll i=1LL<<30;i<1LL<<31;i++){
    //for(ll i=1;i<1LL<<30;i++){
        if (is_palindrome(i) && is_palindrome(i*i))
            cout<<i<<" " << i*i << endl;
    }*/
    for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        ll A,B;
        cin>>A>>B;
        ll counter = 0;
        ll i = 0;
        ll i2 = 0;
        while (i2<B) {
            i++;
            i2=i*i;
            if (i2<A ||i2>B)
                continue;
            if (is_palindrome(i) && is_palindrome(i2))
                counter ++;
        }

        cout << "Case #"<<caseId<<": "<<counter<<endl;
	}
    return 0;
}