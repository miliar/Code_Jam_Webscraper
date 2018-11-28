#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<cmath>
#include<iomanip>
#include<cstdlib>
#include<sstream>
#include<climits>
#include<cassert>
#include<time.h>
using namespace std;
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define pb push_back
#define ss second
#define ff first
#define vi vector<int>
#define vl vector<ll>
#define s(n) scanf("%d",&n)
#define ll long long
#define mp make_pair
#define PII pair <int ,int >
#define PLL pair<ll,ll>
#define inf 1000*1000*1000+5
#define v(a,size,value) vi a(size,value)
#define sz(a) a.size()
#define all(a) a.begin(),a.end()
#define tri pair < int , PII >
#define TRI(a,b,c) mp(a,mp(b,c))
#define xx ff
#define yy ss.ff
#define zz ss.ss
#define in(n) n = inp()
#define vii vector < PII >
#define vll vector< PLL >
#define viii vector < tri >
#define vs vector<string>
#define DREP(a) sort(all(a)); a.erase(unique(all(a)),a.end());
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
#define ok if(debug)
#define trace1(x) ok cerr << #x << ": " << x << endl;
#define trace2(x, y) ok cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)    ok      cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)  ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
								<< #d << ": " << d << endl;
#define trace5(a, b, c, d, e) ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
									 << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
									<< #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
ll MOD = int(1e9) + 7;

int debug = 0;
const int N = 2*int(1e5) + 5;
using namespace std;
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
char c[4] = {'^' , '<' , 'v' , '>'};
int m,n;
int check(string a[105] , int x , int y , int dir)
{
      int x1 = x + dx[dir] , y1 = y + dy[dir];
      while(x1 < m && y1 < n && x1 >= 0 & y1 >= 0)
      {
            if(a[x1][y1] != '.')
                  return 1;
            x1 += dx[dir];
            y1 += dy[dir];
      }
      return 0;
}
int check1(string a[105] , int x , int y)
{
      int i;
      rep(i,4)
            if(c[i] == a[x][y])
                  return check(a,x,y,i);
}
int main()
{
      int i,j,t;
      ios::sync_with_stdio(false);
      cin>>t;
      int t1 = 0;
      for(t1 = 1; t1 <= t; t1++)
      {

            cin>>m>>n;
            string a[105];
            rep(i,m)
                  cin>>a[i];
            int ans = 0 , flag = 0;
            rep(i,m)
                  rep(j,n)
                  {
                        if(a[i][j] == '.')
                              continue;
                        int k;
                        int ch1 = 0;
                        rep(k,4)
                              if(check(a ,i,j, k) != 0)
                                    ch1 = 1;
                        if(ch1 == 0)
                              flag = 1;
                        else
                              if(!check1(a,i,j))
                                    ans++;
                  }
            if(flag == 1)
                  cout<<"Case #"<<t1<<": "<<"IMPOSSIBLE"<<endl;
            else
                  cout<<"Case #"<<t1<<": "<<ans<<endl;
      }
}
