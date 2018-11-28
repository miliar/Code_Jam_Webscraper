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

#define QX "A"

char mm[256];

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
        int cd[4][4],cd2[4][4];
        int mk[17];
        cl(mk, 0);
        int row,row2;
        cin>>row;
        rep(i,4){
            rep(j,4){
                cin>>cd[i][j];
                if (i==row-1) {
                    mk[cd[i][j]]=1;
                    //cout<<cd[i][j]<<" ";
                }
            }
        }
        cin>>row2;
        int matched = 0;
        int ans=-1;
        rep(i,4){
            rep(j,4){
                cin>>cd2[i][j];
                if (row2-1==i && mk[cd2[i][j]]) {
                    matched++;
                    ans=cd2[i][j];
                    //cout<<ans<<endl;
                }
            }
        }

        // output
        if (matched==1)
            cout << "Case #"<<caseId<<": "<<ans<<endl;
        else if (matched>1)
            cout << "Case #"<<caseId<<": "<<"Bad magician!"<<endl;
        else
            cout << "Case #"<<caseId<<": "<<"Volunteer cheated!"<<endl;
	}
    return 0;
}