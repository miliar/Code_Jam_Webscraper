#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 100100
#define mod 1000000007
#define MS0(x) memset(x, 0, sizeof(x))
#define ll long long int
#define in(x) scanf("%I64d", &x)
#define ind(x) scanf("%d", &x)

using namespace std;
int main()
{
    #ifndef ONLINE_JUDGE
#endif
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);

	 ios_base::sync_with_stdio(false);
 cin.tie(NULL);
    int tc,t;
    cin>>tc;
    for(t=1;t<=tc;t++)
    {
          int n,x,s=0,i;
          cin>>n;
          vector<string> v;
          pair<int,string> p[28];
          char c[27]={'0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

          for(i=1;i<=n;i++)
          {
          	cin>>x;
          	p[i].first=x;
          	s=s+x;
          	p[i].second=c[i];
          }
           sort(p+1,p+n+1);
         //  cout<<s<<"\n";
           if(s%2==0)
           {
           while(s>1)
          {
          	sort(p+1,p+n+1);
             p[n].first--;
             p[n-1].first--;
             s=s-2;
             string x=p[n].second;
                string y=p[n-1].second;
                   string z=x+y;
             v.push_back(z);
             }
  
          int si=v.size();
           cout<<"Case #"<<t<<": ";
          for(i=0;i<si-1;i++)
          {
              cout<<v[i]<<" ";
          }
          cout<<v[si-1]<<"\n";
           }
          else  if(s%2==1)
           {
           	sort(p+1,p+n+1);
             p[n].first--;
             s=s-1;
             string x=p[n].second;
                   string z=x;
             v.push_back(z);
           while(s>1)
          {
          	sort(p+1,p+n+1);
             p[n].first--;
             p[n-1].first--;
             s=s-2;
             string x=p[n].second;
                string y=p[n-1].second;
                   string z=x+y;
             v.push_back(z);
             }
  
          int si=v.size();
           cout<<"Case #"<<t<<": ";
          for(i=0;i<si-1;i++)
          {
              cout<<v[i]<<" ";
          }
          cout<<v[si-1]<<"\n";
           }
     
    }
	return 0;
}
