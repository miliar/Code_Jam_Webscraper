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

int M,N;

 vector<string> C[5];
vector<int> process(int k)
{
    vector<int > ret;
    while(k>0)
    {
        ret.push_back(k%N);
        k/=N;
    }
    for(int i= ret.size(); i<M; i++)
        ret.push_back(0);
    reverse(ret.begin(), ret.end());
    return ret;
}

// 分别处理每一个 Vectgor<string> 求节点数.
int pro()
{
    int ret = 0;
    for(int i=0; i<N; i++)
    {
        int tmpret = 0;
        set<string> c;
        c.clear();
        for(int j=0; j<C[i].size(); j++)
        {
            for(int k=1; k<=C[i][j].size(); k++)
                c.insert(C[i][j].substr(0,k));
        }
        if(c.size() == 0) continue;
        ret += c.size()+1;
    }
    return ret;
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D-small-attempt2.out","w",stdout);
    int T; cin>>T;
    for(int cas = 1; cas<=T ; cas++)
    {
//        int M; int N;
        cin>>M>>N;
        vector<string> x(M);
        for(int i=0; i<M; i++) cin>>x[i];
        // M 位 N进制数.

        for(int i=0; i<N; i++) C[i].clear();

//        cout<<"CAS "<<endl;
        int all = pow(N,M);
//        cout<<"! "<< all<<endl;
        int maxret = 0;
        int maxnum = 0;
        for(int i=0; i<all; i++)
        {
//            cout<<"i "<<i<<endl;
            vector<int> dit = process(i);
            for(int i=0; i<N; i++) C[i].clear();
            for(int j=0; j<dit.size(); j++)
                C[dit[j]].push_back(x[j]);
//            for(int j = 0; j<dit.size(); j++) cout<<dit[j]<<" "; cout<<endl;
            int tmp = pro();
//            cout<<"ret "<<tmp<<endl;
            if(tmp == maxret) maxnum++;
            else if(tmp > maxret)
            {
                maxret = tmp; maxnum = 1;
            }
        }
        cout<<"Case #"<<cas<<": "<<maxret<<" "<<maxnum<<endl;
    }
    return 0;
}
