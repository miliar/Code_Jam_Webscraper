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
#define inf INT_MAX
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define PQ priority_queue
#define F first
#define S second
#define EPS 1e-11
#define hi 1010

///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;

double a1[hi],a2[hi];


int main()
{
     #if defined( rifat_pc )
        Write("out.txt");
        Read("D-large.in");
    #endif
    int tst,cnt=1;
    cin>>tst;
    while(tst--){
        double val;
        int n;
        cin>>n;
        rp(i,n){
            scanf("%lf",&val);
            a1[i]=val;
        }
        rp(i,n){
            scanf("%lf",&val);
            a2[i]=val;
        }
        sort(a1,a1+n);
        sort(a2,a2+n);
        int y,z;
        y=z=0;
        bool vis[hi];
        ms(vis,1);
        int id;
        double mn;
        rp(i,n){
            for(int j=n-1;j>=0;j--){
                if(vis[j] && a1[i]>a2[j]){
                    vis[j]=0;
                    y++;
                    break;
                }
            }
        }
        ms(vis,1);
        rp(i,n){
            for(int j=n-1;j>=0;j--){
                if(vis[j] && a2[i]>a1[j]){
                    vis[j]=0;
                    z++;
                    break;
                }
            }
        }
        z=n-z;
        printf("Case #%d: %d %d\n",cnt++,y,z);
    }


    return 0;
}



