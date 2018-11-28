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
#define st(N,pos) ( N | (1<<pos))
#define ck(N,pos) ((bool)(N & (1<<pos)))
#define i_s(num)  static_cast<ostringstream*>( &(ostringstream() << num) )->str();
#define inf INT_MAX
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define PQ priority_queue
#define F first
#define S second
#define bits(n) __builtin_popcount(n)
#define EPS 1e-11
#define hi 110
#define md 1000000007
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;


string s[hi];
int ans[hi];
LL st[(1<<10)+11][30];
int n;
LL bm(int msk,int lst)
{
    if(msk == (1<<n)-1)
    {
        return 1;
    }
    if(lst>0&&st[msk][lst]!=-1)return st[msk][lst];
    int ret=0;
    for(int i=0; i<n; i++)
    {

        if(ck(msk,i)==0)
        {

            int cur = st(msk,i);
            int ok=0;
            rp(j,n)
            {
                if(ck(msk,j)==1)
                {
                    ok=ok|ans[j];
                }
            }
            int b1=bits(ok);
            int b2=bits(ans[i]);
            int b3= bits(ok|ans[i]);
            bool m=0;
            if(lst>-1&& s[lst][s[lst].size()-1]==s[i][0])
            {
                if(b3==b1+b2-1)
                {

                    m=1;
                }

            }
            else if(b3==b1+b2)m=1;
            if(m)ret+=bm(cur,i);
            ret%=md;
        }
    }
    return st[msk][lst]=ret;
}

int main()
{
#if defined( rifat_pc )
    Write("out.txt");
    Read("B-small-attempt1.in");
#endif

    int tst,cnt=1;
    cin>>tst;
    while(tst--)
    {
        cin>>n;
        rp(i,n)
        {
            cin>>s[i];

        }
        ms(ans,0);
        set<char> x;
        bool ok=1;
        rp(i,n)
        {
            x.clear();
            int cur=0,prev=0;
            rp(j,s[i].size())
            {
                x.insert(s[i][j]);
                cur=x.size();
                if(j && cur==prev)
                {
                    if(s[i][j]!=s[i][j-1])ok=0;
                }
                prev=cur;
            }
        }
        rp(i,n)
        {
            rp(j,(int)s[i].size())
            ans[i]=st(ans[i],(int)(s[i][j]-'a'));
        }
        ms(st,-1);
        int ans1=0;
        if(ok)
        {
            ans1 = bm(0,-1);
        }
        cout<<"Case #"<<cnt++<<": "<<ans1<<endl;

    }


    return 0;
}




