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

const LL MOD = 1000002013LL;

LL getValue(LL d, LL n) {
    if(d==0)    return 0;
    LL m = (n*(n+1))/2;
    LL m2 = ((n-d)*(n+1-d))/2;
    return (m-m2)%MOD;
}

map<LL,LL> update(map<LL,LL> mCount, int last, int cur) {
    if(last==cur)   return mCount;
    map<LL,LL> ret;
    FR(it,mCount) {
        ret[(*it).f-(cur-last)] = (*it).s;
    }
    return ret;
}

int main(){
    int t;
    LL n,m,p;
    cin>>t;
    FF(kase,1,t+1){
        cout<<"Case #"<<kase<<": ";
        cin>>n>>m;
        map<int,LL> st, en;
        set<int> pts;
        LL rc = 0;
        while(m--) {
            int o,e;
            cin>>o>>e>>p;
            st[o] += p;
            en[e] += p;
            pts.insert(o);
            pts.insert(e);
            rc = (rc + getValue(e-o,n)*p) % MOD;
        }
//        cout<<rc<<endl; 
        
        LL up = 0;
        map<LL,LL> mCount;
        int last = 0;
        FR(it, pts) {
            
  //          FR(it2,mCount) {
    //            cout<<(*it2).first<<" :: "<<(*it2).second<<endl;
      //      }
            
            int pt = (*it);
            if(mCount.size()>0) {
                FR(it2,mCount) {
                    up += (getValue(pt-last,(*it2).f-1) * (*it2).s) % MOD;
 //                   cout<<(*it2).f-1<<" "<<pt-last<<" - "<<getValue(pt-last,(*it2).f-1)<<endl;
                    up %= MOD;
                }
   //             cout<<pt<<"=="<<up<<endl;

                mCount = update(mCount, last, pt);
                
          //      FR(it2,mCount) {
            //        cout<<(*it2).first<<" -- "<<(*it2).second<<endl;
              //  }
            }
            last = pt;
            
            if(st.find(pt)!=st.end()) {
                mCount[n+1] = st[pt];
            }
            
            if(en.find(pt)!=en.end()) {
                LL ct = en[pt];
                while(ct>0) {
                    int maxKey = (mCount.rbegin()->first);
  //                  cout<<pt<<" ... "<<maxKey<<endl;
                    LL cnt = mCount[maxKey];
                    if(cnt<=ct) {
                        ct -= cnt;
                        mCount.erase(maxKey);
                    } else {
                        mCount[maxKey] -= ct;
                        break;
                    }
                }
            }
        }
        cout<<((rc-up)%MOD+MOD)%MOD<<endl;
//        return 0;
    }
    return 0;
}
