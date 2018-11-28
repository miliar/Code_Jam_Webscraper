#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <utility>
#include <cstdlib>
#include <cassert>

#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define EPS 1e-9

using namespace std;

typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef unsigned long long ull;

ull len(ull x)
{
    return (ull)ceil(log10((double)x)+EPS);
}

ull pow10(const ull &exp)
{
    return pow((ull)10,exp);
}

ull pow(const ull &x, const ull &exp)
{
    assert(exp>=0);
    switch(exp)
    {
        case 0:return 1;
        case 1:return x;
        default:return pow(pow(x,exp/2),2)*pow(x,exp%2);
    }
}

ull make(ull x, bool even)
{
    ull t=x,y=0;
    if(!even)t/=10;
    while(t>0)
    {
        y=y*10+t%10;
        t/=10;
    }
    //cout<<y+x*pow(10,len(x)-1)<<endl;
    if(even)return y+x*pow10(len(x));
    else return y+x*pow10(len(x)-1);
}

bool fair(ull x)
{
    vector<ull> digits;
    while(x>0){
        digits.pb(x%10);
        x/=10;
    }
    bool f=true;
    rep(i,digits.size()/2)
        if(digits[i]!=digits[digits.size()-i-1])f=false;
    //if(f){rep(i,digits.size())cout<<digits[i];cout<<' ';}
    return f;
}

int main()
{
    //freopen("C.txt","r",stdin);
    freopen("C-small.in","r",stdin);
    //freopen("C-large.in","r",stdin);
    freopen("C-output.txt","w",stdout);
    int T;
    cin>>T;
    rep(TI,T)
    {
        ull l,r;
        cin>>l>>r;
        int cnt=0;
        for(ull i=1;;i++)
        {
            ull t=make(i,true);
            t*=t;
            if(t<l)continue;
            if(t<=r)
            {
                if(fair(t))
                {
                    //cout<<make(i,true)<<' ';
                    if(cnt++%10==0);//cout<<endl;
                }
            }
            t=make(i,false);
            t*=t;
            if(t>r)break;
            if(t>=l)
            {
                if(fair(t))
                {
                    //cout<<make(i,false)<<' ';
                    if(cnt++%10==0);//cout<<endl;
                }
            }
        }
        printf("Case #%d: %d\n",TI+1,cnt);
    }
    return 0;
}
