/*
 *
 */
#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mod 1000000007

int main()
{
  int t,d,c,r,s,w,i=1;
  cin>>t;
  while(t--){
    cin>>r>>c>>w;
    d = c -w;
    s = (d%w==0)?d/w:(d/w)+1;
    cout<<"Case #"<<i<<": "<<s+w<<endl;
    i++;
  }
  return 0;
}
