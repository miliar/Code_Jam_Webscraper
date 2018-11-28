#include<bits/stdc++.h>
using namespace std;

typedef long long int LL;

#define inp_s     ios_base::sync_with_stdio(false)
#define DRT()     int test_case;cin>>test_case;while(test_case--)

#define VI        vector<int>
#define VS        vector<string>
#define VLL       vector<LL>
#define PII       pair<int,int>
#define all(c)    c.begin(),c.end()
#define sz(c)     c.size()
#define clr(c)    c.clear()
#define msi       map<string,int>
#define msit      map<string,int>::iterator
#define pb        push_back
#define mp        make_pair

#define GI(x)     scanf("%d",&x)

#define FOR(i,a,b)      for(int i=(a);i<(b);i++)
#define RFOR(i,a,b)     for(int i=(b)-1;i>=(a);i--)

#define gcd(a,b)  __gcd(a,b)
#define MOD       1000000007
#define EPS       1E-10
#define ELR       2.71828182845904523536
#define PI        acos(-1)

#define CASE(x)   fout << "Case #" << x << ": "

int main()
{
      ifstream fin("B.in");
      ofstream fout("B.txt");
      int t;
      fin >> t;
      int p = 0;
      while(t--)
      {
            int n;
            fin >> n;
            VI arr(n);
            FOR(i,0,n) fin >> arr[i];
            int ans = INT_MAX;
            FOR(i,1,1001)
            {
                  int temp = i;
                  FOR(j,0,n)
                  {
                        if(arr[j] <= i) continue;
                        else temp += ((arr[j] + i - 1) / i) - 1;
                  }
                  ans = min(ans,temp);
            }
            ++p;
            CASE(p);
            fout << ans << endl;
      }
      return 0;
}
