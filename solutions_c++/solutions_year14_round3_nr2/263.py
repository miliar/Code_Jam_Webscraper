#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define For(i,N) for(int i=0; i<N; i++)
#define Fore(i,C) for(__typeof((C).begin()) i =(C).begin(); i != (C).end(); ++i)
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define Fors(i,s) for(int i=0; s[i]; i++)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef long long ll;
using namespace std;

int T;

ll mod = 1000000007LL;

vector<ll> P;
vector<int> W,C;
vector<ll> fak(1000);


char buf[200];
int N;

char zac(char *c){ return c[0]; }
char kon(char *c){ return c[strlen(c)-1];}

string mid(char *c){
  int len = strlen(c);
  int z=1;
  while(c[z] && c[z]==c[0]) z++;
  int k=len-2;
  while(k>=0 && c[k]==c[len-1]) k--;
  string s="";
  for(int i=z; i<=k; i++) s+= c[i];
  return s;
}

bool save_valid(char z, char k){
  if(z==k){
    int i = z-'a';
    if(C[i] == 2) return 0;
    else C[i] = 1;
    P[i]++;
  }
  else{
    int iz = z-'a', ik = k-'a';
    if(C[iz] == 2 || C[ik] == 2) return 0;
    else{ C[iz] = 1; C[ik] = 1; }
    
    if( W[iz] != -1) return 0;
    else W[iz] = ik;
  }
  return 1;
}

int main(){
  fak[0] = 1;
  FOR(i,1,fak.size()) fak[i] = ( fak[i-1] * ll(i) ) % mod;
  scanf(" %d", &T);
  For(t,T){
    bool ok = 1;
    P.clear();	P.resize(26,0);
    W.clear();	W.resize(26,-1);
    C.clear();	C.resize(26,0);
    
    scanf(" %d", &N);
    For(n,N){
      scanf(" %s", buf);
      char z = zac(buf);
      char k = kon(buf);
      string s = mid(buf);
      
      if(s != "") 
	FOR(i,1,int( s.size() )+1) if(i==int(s.size()) || s[i] != s[i-1]){
	  int ic = s[i-1] - 'a';
	  if(C[ic] != 0) ok = 0;
	  else C[ic] = 2; 
	}  
      
      ok = ok && save_valid(z,k); 
      if(z==k && s != "") ok=0;
    }
    
    vector<int> bol(26,-1); //unikatnost koncov a pozicie bol[char] - v ktorom je ako koniec
    For(i,26) if(W[i] != -1){
      if(bol[ W[i] ] != -1) ok=0;
      else bol[ W[i] ] = i;
    }
    
    if( !ok){printf("Case #%d: 0\n",t+1); continue;}
    
    vector<bool> pouzite(26,0);
    vector<ll> moznosti;
    
    For(i,26) if( !pouzite[i] && ( W[i] != -1 || bol[i] !=-1)){
      ll moz = fak[ P[i] ];
      int cur = i;
      pouzite[cur] = 1;
      
      if(W[i] != -1){
	cur = W[cur];  
	while(1){
	  if(pouzite[cur]){  ok = 0; break; }
	  pouzite[cur] = 1;
	  moz = ( moz * fak[P[cur]] ) % mod;
	  if( W[cur] == -1 ) break;
	  else cur = W[cur];
	}
      }
      
      if(bol[i] != -1){
	cur = bol[i];
	while(1){
	  if(pouzite[cur]){ok = 0; break; }
	  pouzite[cur] = 1;
	  moz = ( moz * fak[P[cur]] ) % mod;
	  if(bol[cur] == -1) break;
	  else cur = bol[cur];
	}
      }
      
      moznosti.pb(moz);
    }
    
    For(i,26) if(!pouzite[i] && C[i] == 1) moznosti.pb( fak[ P[i] ] );
    
    if( !ok){printf("Case #%d: 0\n",t+1); continue;}
    
    ll vys = 1LL;
    For(i,moznosti.size()) vys = (vys * moznosti[i]) % mod;
    vys = ( vys * fak[ int(moznosti.size()) ] ) % mod;
    
    printf("Case #%d: %lld\n", t+1, vys);
  }
  return 0;
}