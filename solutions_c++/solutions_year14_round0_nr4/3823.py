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
  int T,N,count;
  double naomi[1009],ken[1009];
  int nn[1009],kk[1009];
  cin>>T;
  rep(t,T)
  {
    cin>>N;
    rep(i,N)
    {
      cin>>naomi[i];
    }
    rep(i,N)
    {
      cin>>ken[i];
    }
    sort(naomi,naomi+N);
    sort(ken,ken+N);
    cout<<"Case #"<<t+1<<": ";
    memset(nn,0,sizeof(nn));
    memset(kk,0,sizeof(kk));
    count=0;
    rep(i,N)
    {
      int found=0;
      rep(j,N)
      {
        if(ken[i]<naomi[j]&&nn[j]!=1)
        {
          nn[j]=1;
          kk[i]=1;
          count++;
          found=1;
          break;
        }
      }
      if(found==0)
      {
        rep(j,N)
        {
          if(nn[j]!=1)
          {
            nn[j]=1;
            kk[i]=1;
            break;
          }
        }
      }
    }
    cout<<count<<" ";
    memset(nn,0,sizeof(nn));
    memset(kk,0,sizeof(kk));
    count=0;
    rep(i,N)
    {
      int found=0;
      rep(j,N)
      {
        if(naomi[i]<ken[j]&&kk[j]!=1)
        {
          nn[i]=1;
          kk[j]=1;
          found=1;
          break;
        }
      }
      if(found==0)
      {
        rep(j,N)
        {
          if(kk[j]!=1)
          {
            nn[i]=1;
            kk[j]=1;
            count++;
            break;
          }
        }
      }
    }
    cout<<count<<endl;
  }
  return 0;
}

