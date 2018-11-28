#include<bits/stdc++.h>
#define ll long long int
#define ull unsigned long long
#define pb push_back
#define in     insert
#define all(v) v.begin(),v.end()
#define loop(i,n) for(int i=0;i<n;i++)
#define TC()      ull t;cin>>t;while(t--)
#define mk make_pair
#define sz(a) int((a).size())
#define umap unordered_map
#define endl '\n'
#define vitr vector<ll>::iterator
#define sitr set<ll>::iterator
#define inf LLONG_MAX
#define minf LLONG_MIN
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define gc getchar
#define MOD 1000000007
#define F first
#define S second

using namespace std;
void FastIO(){ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);}

int read_int() {
  char c = gc ();
  while(c<'0' || c>'9') c = gc();
  int ret = 0;
  while(c>='0' && c<='9') {
    ret = 10 * ret + c - 48;
    c = gc();
  }
  return ret;
}
string str;
int solve(void)
{
	int sz=str.size();
	int ct=0;
	loop(i,sz-1)
		if(str[i]!=str[i+1]) ct++;
	if(str[sz-1]=='-') ct++;
	
	return ct;
}
int main()
{
  FastIO();
   ifstream cin("inputfile.txt");
  ofstream cout("out.txt");
  
  int t,T;
  
  cin>>T;
  for(int t=1;t<=T;t++)
  {
  	cin>>str;
      cout <<"Case #"<<t<<": "<<solve()<<endl;
    
  }
  return 0;
}

