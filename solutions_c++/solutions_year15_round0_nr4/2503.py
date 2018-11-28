# include <iostream>
# include <fstream>
# include <sstream>
# include <algorithm>
# include <cstdio>
# include <cmath>
# include <numeric>
# include <cstdlib>
# include <cstring>
# include <vector>
# include <list>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <cctype>
# include <climits>
# include <complex>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define mp make_pair
#define inf 1000000000
#define mod 1000000007
#define mst(a,b) memset(a,b,sizeof(a))
#define pi (double)(3.141592653589793)


int main()
{
      freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int i,j,k,x,r,c,t;
  cin>>t;
  rep(i,1,t+1)
  {
      cin>>x>>r>>c;
      if(x==1 && r!=0 &&c!=0)
      {
          cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
      }
     else if(x==2) {
            if(((r*c))%2==0)
            {
                 cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
            }
            else
                 cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;

      }
      else if(x==3)
      {
          if((((r*c))%3!=0) || min(r,c)==1)
             cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
          else
             cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
      }
      else{
        if((((r*c))%4!=0) || min(r,c)==1 || min(r,c)==2)
             cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
              else
             cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;

      }
  }

    return 0;
}
