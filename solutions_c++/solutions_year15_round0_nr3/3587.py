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

int main()
{
//	freopen("" QX ".txt","r",stdin);
//	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
//	freopen("" QX "-large-1.in","r",stdin);freopen("" QX "-large-1.out","w",stdout);

    int T=0;
	scanf("%d",&T);
    for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        char M[255][255];
        M['1']['1'] = '1'; M['1']['i'] = 'i'; M['1']['j'] = 'j'; M['1']['k'] = 'k';
        M['i']['1'] = 'i'; M['i']['i'] = -'1'; M['i']['j'] = 'k'; M['i']['k'] = -'j';
        M['j']['1'] = 'j'; M['j']['i'] = -'k'; M['j']['j'] = -'1'; M['j']['k'] = 'i';
        M['k']['1'] = 'k'; M['k']['i'] = 'j'; M['k']['j'] = -'i'; M['k']['k'] = -'1';

        int L,X;
        cin>>L>>X;
        char ch[10001];
        rep(i,L) {
            cin>>ch[i];
        }
        int N = L*X;
        int k = 0;
        rep(i,X) {
            rep(j,L) {
                ch[k++] = ch[j];
            }
        }
        char f = 'i';
        char p = 0;
        int i = 0;
        while (i < N) {
            if (p==0) {
                p=ch[i++];
            }
            if (f == 'i' || f == 'j') {
                if (p == f) {
                    f++;
                    p=0;
                    continue;
                }
            } else {
            }
            if (i == N) break;
            int sgn=1;
            if (p<0) {
                p=-p;
                sgn=-1;
            }
            p = sgn*M[p][ch[i++]];
        }

        //edge case
        if (f=='k' && p=='k') {
            cout << "Case #"<<caseId<<": YES"<<endl;
        } else {
            cout << "Case #"<<caseId<<": "<<"No"<<endl;
        }
	}
    return 0;
}