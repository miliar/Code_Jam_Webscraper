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
  int t,cum,ans,n,i,j,req;
  string s;
  cin>>t;
  for(j=1;j<=t;j++){
    cin>>n;
    cin>>s;
    cum=0;
    ans=0;
    for(i=0;i<=n;i++){

      if((s[i]-'0')!=0){

	req = i - cum;
	if(req>0){
	  ans+=req;
	  cum+=req;
	}
	cum+= s[i]-'0';
      }
    }
    cout<<"Case #"<<j<<": "<<ans<<endl;
  }
  return 0;
}
