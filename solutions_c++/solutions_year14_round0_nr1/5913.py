#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef set<int> sI;
typedef set<pI> spI;
typedef priority_queue<int> qmax;
typedef priority_queue<int, vector<int>, greater<int> >qmin;
typedef map<int, int>::iterator mI_it;
typedef set<int>::iterator sI_it;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define B begin()
#define E end()
#define F0(i, n) for( int (i) = 0; (i) < (n); (i)++)
#define F1(i, n) for( int (i) = 1; (i) <= (n); (i)++)
#define zero(i) memset((i),0,sizeof((i)))

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int ioo = (~0)-(1<<31);
const LL loo = (~(LL)0)-((LL)1<<63);

int main()
{
    freopen("out.txt","w",stdout);
    freopen("A-small-attempt0.in","r",stdin);
    int t, test = 0;
    cin>>t; 
    while(t--)
    {
        int k1, k2; cin>>k1;
        int a[5][5], b[5][5];
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                cin>>a[i][j];
        cin>>k2;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                cin>>b[i][j];
        int flag[20] = {0};
        for(int i = 1; i <= 4; i++)
            flag[a[k1][i]]++;
        for(int i = 1; i <= 4; i++)
            flag[b[k2][i]]++;
        int ans = -1;
        int c = 0;
        for(int i = 1; i <= 16; i++){
            if(flag[i] > 1){
                ans = i;
                c++;
            }
        }
        cout<<"Case #"<<++test<<": ";
        if(c == 0) cout<<"Volunteer cheated!"<<endl;
        if(c == 1) cout<<ans<<endl;
        if(c > 1) cout<<"Bad magician!"<<endl;
    }
    return(0);
}

