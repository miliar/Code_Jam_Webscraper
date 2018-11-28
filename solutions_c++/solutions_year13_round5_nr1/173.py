/*	SURENDRA KUMAR MEENA	*/
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
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define f first
#define s second

int b,n;
vector<PI> v;

bool cmp(PI x, PI y) {
    if(x.f==y.f)    return x.s<y.s;
    return x.f<y.f;
}

double getProfit() {
    while(v.size()<37)  v.push_back(PI(0,0));
    double ans = 0.0;
    sort(ALL(v),cmp);
    FF(d,1,b+1) {
        v[0].f++;
        v[0].s++;
        sort(ALL(v),cmp);
        int cnt=1;
        FF(i,1,v.size()) {
            if(v[i].f!=v[i-1].f)    break;
            cnt++;
        }
        double val = 0.0;
        F(i,cnt) {
            val += 36.0*v[i].s;
        }
        val /= cnt;
  //      cout<<cnt<<endl;
//        cout<<d<<" : "<<val-d<<endl;
        ans = max(ans, val-d);
    }
    return ans;
}

int main(){
    int t;
    cin>>t;
    FF(kase,1,t+1){
        cout<<"Case #"<<kase<<": ";
        v.clear();
        cin>>b>>n;
        F(i,n) {
            int k;
            cin>>k;
            v.push_back(PI(k,0));
        }
        printf("%.8lf\n",getProfit());
    }
    return 0;
}

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
