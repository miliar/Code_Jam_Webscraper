#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define bg begin()
#define en end()
#define Y second
#define X first
typedef long long ll;
 
#define fi freopen("input.txt","r",stdin)
#define fo freopen("output.txt","w",stdout)
 
const double pi     =   acos(-1.0);
const double eps    =   1e-8;
 
#define print(a) cout<<(#a)<<" = "<<a<<"\n";
#define fill(a,val) memset(a ,val, sizeof(a) );
#define sz(s) ((int)(s.size()))
/*Solution code starts here */


void solve( int test )
{
	int mx ;
	string in;

	cin>>mx>>in;

	int mila =0;
	int ans =0;

	for(int req=0;req<=mx;req++)
	{
		    if( in[req]!='0')
		    {
		    	int diff = max(0,req-mila);//itna bulana padega
				ans+=diff;
				mila+=(in[req]-'0');//yaha wale ho jor lia
				mila+=diff;//bulaya use bhi jod lia
			}
    }

    printf("Case #%d: %d\n",test,ans);
}

int main()
{
   int test;

   cin>>test;

   for(int i=1;i<=test;i++)
   {
   	solve(i);
   }

   return 0;
}