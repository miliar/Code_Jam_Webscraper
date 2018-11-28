#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <new>
#include <string>

using namespace std;

#define GETC getchar_unlocked()
inline void fastRead(int *a)
{
 register char c=0;
 int sign=1;
 while (c<33) c=GETC;
 *a=0;
 while (c>33)
 {
    if(c=='-'){sign=-1;}
    else{
     *a=*a*10+c-'0';
    }
     c=GETC;
 }
 *a = *a * sign;
}
 
#define S(__x__) fastRead(__x__)

typedef unsigned long long ULL;

#define N 100005
#define MOD 1000000009


int main() {
    //ios_base::sync_with_stdio(false);
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++) {
        double c,f,mx;
        cin>>c>>f>>mx;
        double ans=0.0;int ck=0;double cr=2.0;
        while(ck<mx) {
            double t1,t2;
            t1=mx/cr;
            t2=c/cr + mx/(cr+f);
            if(t1-t2<0.000000001) {
                //cout<<t1<<endl;
                ans+=t1;break;
            }
            else {
                //cout<<c/cr<<endl;
                ans=ans+c/cr;
                ck=0;
                cr=cr+f;
            }
        }
        printf("Case #%d: %.7lf\n",k,ans);
    //cout<<"Case #"<<k<<": "<<mv<<endl;
    }
    return 0;
}
