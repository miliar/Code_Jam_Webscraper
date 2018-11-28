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
int q[4][4]= {
    {1,2,3,4},
    {2,-1,4,-3},
    {3,-4,-1,2},
    {4,3,-2,-1}
  };

int mul(int a,int b){

  return ((a>0)?1:-1)*(q[abs(a)-1][b-1]);
}
int main()
{
  int t,l,x,v,c,j,i,k;
  string s;
  map <char,int> mymap;
  mymap['i']=2;
  mymap['j']=3;
  mymap['k']=4;
  int g[2] = {2,3};
  cin>>t;
  
  for(i=1;i<=t;i++){
    cin>>l>>x;
    cin>>s;
    v=1;
    c=0;
    for(k=0;k<x;k++){
      for(j=0;j<l;j++){
	v=mul(v,mymap[s[j]]);

	if(v==g[c] && c<2){
	  v=1;
	  c++;
	}
	
      }

    }
    if(v==4 && c==2)
      cout<<"Case #"<<i<<": "<<"YES"<<endl;
    else
      cout<<"Case #"<<i<<": "<<"NO"<<endl;
  }
  return 0;
}
