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

vector <int> v;

int process()
{
  int val,ans=1000000,cnt;
  tr(v,it)
  {
    val=*it;
    cnt=0;
    tr(v,jk)
    {
      cnt+=abs((*jk)-val);
    }
    ans=min(ans,cnt);
  }
  return ans;
}

int main()
{
  string A[200];
  int T,N;
  int cnt[200],flag,ans,tmpcnt;
  cin>>T;
  rep(t,T)
  {
    cin>>N;
    rep(i,N)
      cin>>A[i];
    ans=0;
    memset(cnt,0,sizeof(cnt));
    flag=0;
    rep(i,A[0].length())
    {
      //cout<<i<<" "<<A[0][i]<<endl;
      v.clear();
      for(int j=0;j<N;j++)
      {
        if(A[j][cnt[j]]!=A[0][i])
        {
          flag=1;
          break;
        }
        tmpcnt=0;
        while(A[j][cnt[j]]==A[0][i]&&cnt[j]<A[j].length())
        {
          cnt[j]++;
          tmpcnt++;
        }
        v.PB(tmpcnt);
      }
      ans+=process();
      if(flag==1)
        break;
      i=cnt[0]-1;
    }
    rep(i,N)
    {
      if(cnt[i]!=A[i].length())
      {
        flag=1;
        break;
      }
    }
    cout<<"Case #"<<t+1<<": ";
    if(flag==1)
    {
      cout<<"Fegla Won\n";
    }
    else
    {
      cout<<ans<<endl;
    }
  }
  return 0;
}

