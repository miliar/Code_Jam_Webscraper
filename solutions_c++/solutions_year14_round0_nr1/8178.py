#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#include<numeric>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<list>
#include<climits>
#include<cstdlib>
#include<string>
#include<cmath>

using namespace std;

// useful input/output macros
#define S(n) scanf("%d",&n)
#define SLL(n) scanf("%lld",&n)
#define P(n) printf("%d\n",n)
#define PLL(n) printf("%lld\n",n)
#define SF(n) scanf("%lf\n",&n)
#define PF(n) printf("%lf\n",n)

// useful functions
#define REV(s,e) reverse(s,e)
#define MSET(s,i) memset(s,i,sizeof(s))
#define CPY(i,j) memset(i,j,sizeof(j))
#define MP(x,y) make_pair(x,y)
#define F(i,a,b) for(int i=a;i<b;i++)
#define FK(i,a,b,k) for(int i=a;i<b;i+=k)
#define FR(i,a,b) for(int i=a;i>b;i--)
#define FRK(i,a,b,k) for(int i=a;i>b;i-=k)
#define PB(x) push_back(x)

// shortforms
#define FF first
#define SS second
#define LD long double
#define LI long int
#define LL long long int
#define UG unsigned

// constants
const int inf=1000000007; //prime 
const LD eps=1e-9;
const LD pi=3.141592653589793;
const LD e=2.718281828459045;

///// MAIN CODE NOW /////

vector<int> intersect(vector<int> v,vector<int> w){
  vector<int> ans;
  ans.clear();
  F(i,0,v.size()){
    F(j,0,w.size()){
      if(v[i]==w[j]){
	ans.PB(v[i]);
      }
    }
  }
  return ans;
}

vector<vector<int> > c1,c2;

int main(){
  ios_base::sync_with_stdio(false);
  int t,m,n;
  vector<int> v,w,ans;
  cin>>t;
  c1.resize(4);
  c2.resize(4);
  F(i,0,4){
    c1[i].resize(4);
    c2[i].resize(4);
  }
  F(cas,0,t){
    cin>>m;
    F(i,0,4){
      F(j,0,4){
	cin>>c1[i][j];
      }
    }
    cin>>n;
    F(i,0,4){
      F(j,0,4){
	cin>>c2[i][j];
      }
    }
    v=c1[m-1];
    w=c2[n-1];
    ans=intersect(v,w);
    if(ans.size()==0){
      cout<<"Case #"<<cas+1<<": Volunteer cheated!\n";
    }
    else if(ans.size()==1){
      cout<<"Case #"<<cas+1<<": "<<ans[0]<<endl;
    }
    else{
      cout<<"Case #"<<cas+1<<": Bad magician!\n";
    }
  }
}
