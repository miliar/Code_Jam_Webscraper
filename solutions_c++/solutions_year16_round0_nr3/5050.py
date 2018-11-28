#pragma comment(linker,"/STACK:268435456")
#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <sstream>
#include <bitset>
#include <iterator>
#include <list>
#include <ctime>
#include <functional>
#include <numeric>
#include <cassert>


#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for((cont)::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define VCPRINT(v) for(int iii = 0;iii < (v).size();iii++) cout<<(v)[iii]<<" ";cout<<endl;
#define SETPRINT(v,cont) for((cont)::iterator iiit = (v).begin();iiit != (v).end();iiit++) cout<<*iiit<<" ";cout<<endl;

bool ascending (int i,int j) { return (i<j); }
bool descending (int i,int j) { return (i>j); }

typedef long long ll;
typedef unsigned long long ull;
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PULI pair<unsigned long long,int>
#define PIL pair<int,long long>
#define PSI pair<string,int>
#define PSS pair<string,string>
#define PDD pair<double,double>
#define PIB pair<int,bool>
typedef long double ld;
#define PLI pair<ll,int>

using namespace std;

#define lll __int128

lll powmod(lll a , lll b,lll m){

    lll x=a,p=1;
    while(b>0)
    {
        if(b%2)
            p=((p%m)*(x%m))%m;
        b/=2;
        x=((x%m)*(x%m))%m;
    }
    return p;
}


lll gcd(lll a,lll b)
{
    return b==0?a:gcd(b,a%b);
}


lll composite(lll n,ll k)
{
    lll d = n,r = 0;
    while(d%2==0) d/=2,r++;
    while(k--)
    {
        ll a = 1LL * rand() | rand() << 16;
        a %= (n-3);
        a += 2;
        lll x = powmod(a,d,n);
        if (x == 1 || x == n - 1)
            continue;
        bool flag = false;
        FR(_,r-1)
        {
            x = powmod(x,2,n);
            if(x==1)
                return 1;
            if(x==n-1){
                flag = true;
                break;
            }
        }
        if(!flag) return 1;
    }
    return 0;
}

ull comp(ull a)
{
    for(ull i = 2;i*i <= a;i++)
    {
        if(a%i==0) return i;
    }
    return 0;
}




int main()
{
    ifstream cin("a.in");
    ofstream fout("a.out");
    int T;cin>>T;
    srand((unsigned)time(NULL));
    FOR(_,1,T+1)
    {
        fout<<"Case #"<<_<<":"<<endl;
        int N,J;
        cin>>N>>J;
        set<int> S;
        int cnt = 0;
        FR(R,1<<N)
        {
            R &= (1<<N)-1;
            R |= 1;
            R |= (1<<(N-1));
            bool flag = true;
            vector<int> C;
            for(int b = 2;b <= 10;b++)
            {
                if(!flag) break;
                lll n = 0;
                ull ln = 0;
                ull t = R;
                ull p = 1;
                while(t)
                {
                    n += (t%2)*p;
                    ln += (t%2)*p;
                    p*=b;
                    t/=2;
                }
                lll c = composite(n,100);
                flag = flag && (c>0);
                ull co = comp(ln);
                flag = flag && co;
                C.push_back(co);
            }
            if(flag && J && S.find(R)==S.end()){
                bitset<16> B(R);
                fout<<B<<" ";
                FR(i,C.size()) fout<<C[i]<<" ";
                fout<<endl;
                S.insert(R);
                J--;
            }
            if(J==0) break;
        }
    }
}