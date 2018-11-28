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
      int t;
      LL ans=0;
      string s;
      char state;
      cin >> t;
      for(int i=1;i<=t;i++)
      {
            cin >> s;
            state='+';
            ans=0;
            for(int p=s.length()-1;p>=0;p--)
            {
                  if(s[p]!=state)
                        ans++,state=s[p];
            }
            cout << "Case #" << i << ": " << ans << endl;
      }      
	
	return 0;
}

