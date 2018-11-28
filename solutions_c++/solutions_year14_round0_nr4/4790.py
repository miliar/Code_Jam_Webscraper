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

#define QX "D"

int main()
{
//	freopen("" QX ".txt","r",stdin);
	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
//	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
//	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        set<double> Nao;
        set<double> Ken;
        int N;
        cin>>N;
        rep(i,N) {
            double d;
            cin>>d;
            Nao.insert(d);
        }
        rep(i,N) {
            double d;
            cin>>d;
            Ken.insert(d);
        }
        int war = 0;
        set<double>::const_iterator itK = Ken.begin();
        for (set<double>::const_iterator it = Nao.begin();it!=Nao.end();++it){
            while(itK!=Ken.end() && *itK<*it){
                ++itK;
            }
            if (itK==Ken.end()){
                while(it!=Nao.end()){
                    war++;
                    ++it;
                }
                break;
            } else {
                ++itK;
            }
        }
        itK=Ken.begin();
        int dwar=0;
        for (set<double>::const_iterator it = Nao.begin();it!=Nao.end();++it){
            if (*it>*itK) {
                dwar++;
                ++itK;
            }
        }
        // output
        cout << "Case #"<<caseId<<": "<<dwar<<" "<<war<<endl;
	}
    return 0;
}