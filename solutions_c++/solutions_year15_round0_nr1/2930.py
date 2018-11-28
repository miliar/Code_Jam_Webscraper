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
      ifstream fin("A.in");
      ofstream fout("A.txt");
      int t,p=0;
      fin >> t;
      while(t--)
      {
            VI hasher(1010,0);
            int x;
            fin >> x;
            string s;
            fin >> s;
            FOR(i,0,sz(s)) hasher[i] = s[i] - '0';
            int ans = 0;
            int stood_up = 0;
            FOR(i,0,sz(s))
            {
                  if(stood_up < i)
                  {
                        ans += i-stood_up;
                        stood_up = i;
                  }
                  stood_up += hasher[i];
            }

            ++p;
            CASE(p);
            fout << ans << endl;
      }
      return 0;
}
