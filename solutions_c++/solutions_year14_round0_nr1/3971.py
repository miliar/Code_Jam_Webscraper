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
  int T,A,B,a[4][4],b[4][4],count,ans;
  cin>>T;
  rep(t,T)
  {
    count=0;
    cin>>A;
    A--;
    rep(i,4)
    {
      rep(j,4)
      {
        cin>>a[i][j];
      }
    }
    cin>>B;
    B--;
    rep(i,4)
    {
      rep(j,4)
      {
        cin>>b[i][j];
      }
    }
    rep(i,4)
    {
      rep(j,4)
      {
        if(a[A][i]==b[B][j])
        {
          count++;
          ans=a[A][i];
        }
      }
    }
    cout<<"Case #"<<t+1<<": ";
    if(count==0)
    {
      cout<<"Volunteer cheated!\n";
    }
    else if(count==1)
    {
      cout<<ans<<endl;
    }
    else
    {
      cout<<"Bad magician!\n";
    }
  }
  return 0;
}

