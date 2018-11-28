#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<string>
#include<iostream>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define MOD 1000000007

int T;
int M,N;
string str;
vector<string> S;
vector<string> tmp;
int nodes_needed[550];
int poss;
int maxi;
int nowi;
int sub;

bool done[10];

int need(int from, int to, int first){
  if(from==to) return tmp[from].length()-first;
  if(from>to) return 0;
  int ans=0;
  while(tmp[from].length()<=first) from++;
  int i=from;
  while(i<=to){
    i=from+1;
    while(i<=to && tmp[i][first]==tmp[i-1][first])
      i++;
    ans+=1+need(from,i-1,first+1);
    from=i;
  }
  return ans;
}

int next(int nn, int sdone, int lastadd){
  //printf("nn %d sdone %d nowi %d\n",nn,sdone,nowi);
  if(nn==N){
    //printf("konec? :o, nn %d, sdone %d, M %d\n",nn,sdone,M);
    if(nowi>=maxi){
      maxi=nowi;
      poss = (poss+1)%MOD;
    }
    return 0;
  }
  if(sdone==M && nn<N-1) return 0;
  if(M-sdone>=N-nn){
    FOR(i,lastadd+1,M-1){
      if(done[i]) continue;
      done[i]=true;
      sub+=(1<<i);
      next(nn,sdone+1,i);
      sub-=(1<<i);
      done[i]=false;
    }
  }
  if(sub!=0 && !(nn==N-1 && sdone<M)){
    nowi += nodes_needed[sub];
    int ssub = sub;
    //printf("jdu ke kompu %d se sub %d a nodes %d; sdone %d\n",nn+1,sub,nowi,sdone);
    sub=0;
    next(nn+1,sdone,-1);
    sub = ssub;
    //printf("jdu zpet od kompu %d se sub %d a nodes %d\n",nn+1,sub,nowi);
    nowi -= nodes_needed[sub];
  }
}

int main(){
  scanf("%d",&T);
  FOR(t,1,T){
    //printf("\n\n");
    nowi=maxi=0;
    REP(i,10) done[i]=false;
    S.clear();
    scanf("%d%d",&M,&N);
    REP(i,M){
      cin >> str;
      S.pb(str);
    }
    sort(S.begin(),S.end());
    FOR(i,1,(1<<M)-1){
      tmp.clear();
      //printf("i: %d\nStrings:\n",i);
      REP(j,M) if(i & (1<<j)){
        tmp.pb(S[j]);
        //cout << " " << S[j] << endl;
      }
      nodes_needed[i] = need(0, tmp.size()-1, 0)+1;
      //printf("nodes: %d\n",nodes_needed[i]);
    }
    sub=0;
    maxi=0;poss=0;
    next(0,0,-1);
    sub=0;
    poss=0;
    next(0,0,-1);
    printf("Case #%d: %d %d\n",t,maxi,poss);
  }

  return 0;
}
