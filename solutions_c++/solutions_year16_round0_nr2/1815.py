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
#include <math.h>
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

#define QX "B"

int calc(string cakes)
{
    //cout<<cakes<<endl;
    int l = cakes.length();
    int i = l - 1;
    int c = 0;
    while(i >= 0) {
        while(i >= 0 && cakes[i] == '+') {
            i--;
        }
        if (i < 0) {
            break;
        }
        // check if the first k pieces are all '+'
        int p = 0;
        while(cakes[p] == '+') {
            cakes[p] = '-';
            p++;
        }
        if (p > 0) {
            c ++;
        }
        p = i;
        rep(j,p/2+1) {
            char x=cakes[j];
            cakes[j] = cakes[p-j]=='+'?'-':'+';
            cakes[p-j] = x=='+'?'-':'+';
        }
        c ++;
    }
    return c;
}

int main()
{
//	freopen("../" QX ".txt","r",stdin);
//	freopen("../" QX "-small-attempt0.in","r",stdin);freopen("../" QX "-small-attempt0.out","w",stdout);
//	freopen("../" QX "-small-attempt1.in","r",stdin);freopen("../" QX "-small-attempt1.out","w",stdout);
	freopen("../" QX "-large.in","r",stdin);freopen("../" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        string cakes;
        cin>>cakes;

        // output
        cout << "Case #"<<caseId<<": "<<calc(cakes)<<endl;
        //printf("Case #%d: %.8f\n",caseId,t);
	}
    return 0;
}
