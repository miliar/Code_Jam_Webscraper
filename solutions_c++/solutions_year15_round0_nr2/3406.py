//#include <bits/stdc++.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <numeric>
#include <stack>
#include <functional>
#include <bitset>
#include <iomanip>

#include <ctime>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>
#include <cstdlib>

#define _ ios_base::sync_with_stdio(0);
#define ms(ar,val) memset(ar,val,sizeof(ar))
#define all(s) (s).begin(),(s).end()
#define rp1(i,s,n) for(int i=s;i<n;++i)
#define rp(i,n) rp1(i,0,n)
#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define pb push_back
#define LL long long
#define Read(x) freopen(x,"r",stdin)
#define Write(x) freopen(x,"w",stdout)
#define st(N,pos) (sts[N]=sts[N] | (1<<pos))
#define check(N,pos) ((bool)(sts[N] & (1<<pos)))
#define i_s(num)  static_cast<ostringstream*>( &(ostringstream() << num) )->str();
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define PQ priority_queue
#define GSORT(x) sort(ALL(x), greater<typeof(*((x).begin()))>())
#define UNIQUE(v) sort(all(v)); (v).resize(unique(all(v)) - (v).begin())
#define F first
#define S second
#define bits(n) __builtin_popcount(n)
#define EPS 1e-11
#define PI (atan(1)*4)
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month


using namespace std;
int gcd(int a, int b)
{
    while(b) b ^= a ^= b ^= a %= b;
    return a;
}
#define maxn 1010
priority_queue <int> Q;
int D,P[maxn];
int main()
{
     #if defined( rifat_pc )
        Write("out1.txt");
        Read("B-large.in");
    #endif
    int tst,cnt=1;
    cin>>tst;
    while(tst--){
        cin>>D;
        rp(i,D)cin>>P[i];
        int mx = *max_element(P,P+D);
        int ans =mx;
        for(int i=1;i<maxn;i++){
            int cur = i;
            rp(j,D){
                cur+=(( P[j]-1)/i);
            }
            ans = min(ans,cur);
        }

//        while(!Q.empty())Q.pop();
//
//        rp(i,D)Q.push(P[i]);
//        ans = *max_element(P,P+D);
//
//        rp(i,maxn){
//            int val = Q.top();
//            if(val==1)continue;
//            Q.pop();
//            Q.push(val/2);
//            if(val%2)Q.push(val/2+1);
//            else Q.push(val/2);
//            ans = min(ans,Q.top()+i+1);
//        }
        cout<<"Case #"<<cnt++<<": "<<ans<<endl;

    }


    return 0;
}


//7=4+3=2+2+3=1+2+2+2
