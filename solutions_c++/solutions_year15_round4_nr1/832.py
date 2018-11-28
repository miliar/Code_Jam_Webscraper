#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>
using namespace std;

template<class T> T gcd(T a,T b)
{
    if(a<0) return gcd(-a,b);
    if(b<0)return gcd(a,-b);
    return (b==0)?a:gcd(b,a%b);
}
template <class T> T lcm(T a,T b)
{
    return a*(b/gcd(a,b));
}
template<class T> inline vector<pair<T,int> > factorize(T n)
{
    vector<pair<T,int> > R;
    for (T i=2; n>1;)
    {
        if (n%i==0)
        {
            int C=0;
            for (; n%i==0; C++,n/=i);
            R.push_back(make_pair(i,C));
        }
        i++;
        if (i>n/i) i=n;
    }
    if (n>1) R.push_back(make_pair(n,1));
    return R;
}
template<class T> inline bool isPrimeNumber(T n)
{
    if(n<=1)return false;
    for (T i=2; i*i<=n; i++) if (n%i==0) return false;
    return true;
}
template<class T> inline T eularFunction(T n)
{
    vector<pair<T,int> > R=factorize(n);
    T r=n;
    for (int i=0; i<R.size(); i++)r=r/R[i].first*(R[i].first-1);
    return r;
}
template<class T> string toString(T n)
{
    ostringstream ost;
    ost<<n;
    ost.flush();
    return ost.str();
}
int toInt(string s)
{
    int r=0;
    istringstream sin(s);
    sin>>r;
    return r;
}

int i,j,k;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
int dirx[]= {1, 1, 0,-1,-1,-1,0,1};
int diry[]= {0,-1,-1,-1, 0, 1,1,1}; //clockwise

char M[105][105];

int state[105][105][4];
int main()
{
    ios_base::sync_with_stdio(0);
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T; cin>>T;
    for(int cas = 1; cas<= T; cas++)
    {

        int R, C;
        cin>>R>>C;
        for(int i = 1; i<= R; i++)
        {
            for(int j = 1; j<= C; j++)
                    cin>>M[i][j];
        }
        memset(state, 0, sizeof(state));
        for(int i = 1; i<= R; i++)
        {
            int j = 1;
            while(M[i][j] == '.' && j<=C)
            {
                j++;
            }
            state[i][j][3]=1;
        }

        for(int i = 1; i<=R; i++)
        {
            int j = C;
            while(M[i][j] == '.' && j>=1)
            {
                j--;
            }
            state[i][j][1] = 1;
        }

        for(int j = 1; j<=C; j++)
        {
            int i = 1;
            while(M[i][j] == '.' && i<=R)
                i++;
            state[i][j][0] = 1;
        }
        for(int j = 1; j<= C; j++)
        {
            int i = R;
            while(M[i][j] == '.' && i>=1)
                i--;
            state[i][j][2] = 1;
        }

        int num = 0;
        bool im = 0;
        for(int i = 1; i<=R; i++)
        {
            for(int j =1; j<=C; j++)
            {
                int local = 0;
                for(int k = 0; k< 4; k++)
                    if(state[i][j][k] == 1) local++;
                if(local == 4) im = 1;
                if(M[i][j] == '^' && state[i][j][0]) num++;
                if(M[i][j] == '>' && state[i][j][1]) num++;
                if(M[i][j] == 'v' && state[i][j][2]) num++;
                if(M[i][j] == '<' && state[i][j][3]) num++;
            }
        }

        cout<<"Case #"<<cas<<": ";
        if(im) cout<<"IMPOSSIBLE"<<endl;
        else cout<<num<<endl;
    }

    return 0;
}
