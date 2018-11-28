/////////////////////////////////////////
//  Author : Akshay Jaggi             //
///////////////////////////////////////

#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<utility>
#include<queue>
#include<stack>
#include<string>
#include<cstring>
#include<map>
#define rep(i,N) for(int (i)=0;(i)<(N);(i)++)
#define repi(i,j,N) for(int (i)=(j);(i)<(N);(i)++)
#define repg(i,j,N) for((i)=(j);(i)<(N);(i)++)
#define si(i) scanf("%d",&(i))
#define sl(i) scanf("%lld",&(i))
#define pi(i) printf("%d",(i))
#define pl(i) printf("%lld",(i))
#define pin(i) printf("%d\n",(i))
#define pln(i) printf("%lld\n",(i))
#define pw    printf(" ");
#define pn    printf("\n");

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 



int main()
{
  int T;
  cin>>T;
  long long int P,Q,ans;
  char a;
  rep(t,T)
  {
    cin>>P>>a>>Q;
    ans=-1;
    for(int i=0;i<40;i++)
    {
      P=P*2;
      if(P>=Q)
      {
        if(ans==-1)
        {
          ans=i+1;
        }
        P=P-Q;
      }
    }
    cout<<"Case #"<<t+1<<": ";
    if(P==0&&ans!=-1)
    {
      cout<<ans<<endl;
    }
    else
    {
      cout<<"impossible"<<endl;
    }
  }
  return 0;
}

