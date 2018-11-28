#include <bits/stdc++.h>
using namespace std;
//for cin with white space cin.getline(var,sizeof(var)); with  char var[100];
#define lli long long int
#define pb push_back
#define mp make_pair
#define sd(a) scanf("%lld",&a)
#define pd(a) printf("%lld\n",a)
#define F first
#define S second
// string s= to_string(int ); int to str
//***dont forget to clear the vector using v.clear();***
#define setl set<long long int>
#define sets set<string>
#define msetl multiset<long long int>
#define msets multiset<string>
#define vll vector<lli>
#define vstr vector<string>
#define pii pair<int , int>
#define SZ(x) (int)x.size()
#define len(s) (s.length())
string pk;
int main()
{
    lli l,t,x,y,n,z,m,ans;
   sd(t);

for(x =1; x<=t;x++)
  {
	ans=0;
	cin>>pk;
	l=len(pk);
    for(y=l-1;y>=0;y--)
                {
                    if(pk[y]=='-')
                    {
                        ans++;
                        for(z=y;z>=0;z--)
                        
                            pk[z]=((pk[z]=='-')?'+':'-');
                        
                    }
                }

                printf("Case #%lld: %lld\n",x,ans);
  }
    return 0;

}
