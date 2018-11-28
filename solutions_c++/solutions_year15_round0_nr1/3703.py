#include <bits/stdc++.h>

#define rep(i,n) for(int i=0; i<n; i++)
#define repa(i,a,b,d) for(int i=a; i<=b; i+=d)
#define repd(i,a,b,d) for(int i=a; i>=b; i-=d)
#define repi(it,stl) for(auto it = (stl).begin(); (it)!=stl.end(); ++(it))
#define sz(a) ((int)(a).size())
#define mem(a,n) memset((a), (n), sizeof(a))
#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mt make_tuple
#define tii tuple<int,int>
#define at(t,idx) std::get<(idx)>((t))
#define vi vector<int>
#define vs vector<string>
#define sstr stringstream
#define indexof(v,x) (int((find((v).begin(), (v).end(),(x))-(v).begin() + 1)%((v).size()+1))-1)

typedef long long ll;
using namespace std;

int main()
{
     ios_base::sync_with_stdio(0);
     cin.tie(0);
#ifndef ONLINE_JUDGE
     freopen("main.txt", "rt", stdin);
     freopen("out.txt", "wt", stdout);
#endif

     int tst;
     cin >> tst;

     repa(tt,1,tst,1) {
          int n, sum=0,res=0;
          string str;
          cin >> n >> str;
          n = sz(str);
          rep(i,sz(str)) {
               if (str[i]=='0')continue;
               int add = max(i-sum,0);
               res += add;
               sum += add + (str[i]-'0');
          }
          printf("Case #%d: %d\n",tt,res);
     }
     return 0;
}