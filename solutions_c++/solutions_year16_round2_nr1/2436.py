#include<bits/stdc++.h>
#define MAX 100000
#define nl '\n'
#define pb push_back
#define forn(i,n) for(i=1;i<=n;i++)
#define fornb(i,n) for(i=n;i>=1;i--)
#define for0(i,n) for(i=0;i<n;i++)
#define for0b(i,n) for(i=n-1;i>=0;i--)

typedef long long ll;
typedef double lf;

using namespace std;

string S;

void rd_1()
{
  cin>>S;
}

int main()
{
  ios::sync_with_stdio(0);cin.tie(NULL);
  int i,j,t;
  cin>>t;
  for(j=1;j<=t;j++){
    rd_1();
    int ct[27]={};
    int cnt[10]={};
    int vis[3000]={};
    cout<<"Case #"<<j<<": ";
    int l=S.size();
    for(i=0;i<l;i++)
    {
      ct[S[i] - 'A']++;
    }
    cnt[0]=ct['Z'-'A'];
    cnt[2]=ct['W'-'A'];
    cnt[4]=ct['U'-'A'];
    cnt[6]=ct['X'-'A'];
    cnt[8]=ct['G'-'A'];
    cnt[7]=ct['S'-'A']-cnt[6];
    cnt[5]=ct['F'-'A']-cnt[4];
    cnt[3]=ct['H'-'A']-cnt[8];
    cnt[1]=ct['O'-'A']-cnt[0]-cnt[2]-cnt[4];
    cnt[9]=ct['I'-'A']-cnt[8]-cnt[6]-cnt[5];
    for(i=0;i<10;i++)
    {
      for(int k=0;k<cnt[i];k++)
      {
	cout<<i;
      }
    }
    cout<<nl;
  }
  return 0;
}
