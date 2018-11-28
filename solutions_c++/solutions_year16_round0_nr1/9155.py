#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef vector<int> vi;
typedef vector<pair<int,int> >vpii;
typedef vector <LL> vl;
typedef vector <pair<LL,LL> > vpll;
typedef pair <int,int> pii;
typedef pair <LL,LL> pll;

#define forup(i,a,b) for(int i=(a); i<(b); ++i)
#define fordn(i,a,b) for(int i=(a); i>(b); --i)
#define rep(i,a) for(int i=0; i<(a); ++i)
#define gi(x) scanf("%d ",&x)
#define gll(x) scanf("%lld ",&x)
#define gd(x) scanf("%lf ",&x)
#define gs(x) scanf(" %s",x) 
#define fs first
#define sc second 
#define pb push_back
#define mp make_pair
void setup()
{
      ios_base::sync_with_stdio(false);
      cin.tie(0);
      cout.tie(0);
      cout.precision(15);
}

#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
      cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
      const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define endl '\n'
int main()
{
      //setup();
      LL t,n,a,i;
      cin >> t;
      set<int > s={0,1,2,3,4,5,6,7,8,9};
      set<int > temp;
      for(int c=1;c<=t;c++)
      {
            cin >> n;
            if(n==0)
            {
                  cout << "Case #" << c << ": " << "INSOMNIA" << endl;
                  continue;
            }
            i=1;
            temp=s;
            while(!temp.empty())
            {
                  a=i*n;
                  while(a!=0)
                  {
                        if(temp.find(a%10)!=temp.end())
                              temp.erase(a%10);     
                        a/=10;
                  }
                  i++;
            }
            cout << "Case #" << c << ": " << n*(i-1) << endl;
      }      

      return 0;
}

