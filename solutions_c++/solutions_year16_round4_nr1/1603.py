#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define MODV 1000000007

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;
void addmod(int &a, ll b){a=(a+b); if(a>=MODV)a-=MODV;}
void mulmod(int &a, ll b){a=(a*b)%MODV;}
int gi(){int a;scanf("%d",&a);return a;}
ll gll(){ll a;scanf("%lld",&a);return a;}

char res(char a, char b){
  if(a=='P' && b=='R')return 'P';
  if(a=='R' && b=='P')return 'P';

  if(a=='P' && b=='S')return 'S';
  if(a=='S' && b=='P')return 'S';

  if(a=='R' && b=='S')return 'R';
  if(a=='S' && b=='R')return 'R';
  return 'N';
}

bool can(string s){
  if(s.size()==1)return true;
  int n=s.size();
  string m="";
  for(int i=0;i<n;i+=2){
    if(s[i]==s[i+1])return false;
    m+=res(s[i],s[i+1]);
  }
  return can(m);
}

void doit() {
  int n=gi(), r=gi(), p=gi(),s=gi();
  string m="";
  for(int i=0;i<p;i++){ m+='P'; }
  for(int i=0;i<r;i++){ m+='R'; }
  for(int i=0;i<s;i++){ m+='S'; }
  do{
    if(can(m)){
      cout<<m;
      return;
    }
  }while(next_permutation(m.begin(),m.end()));
  cout<<"IMPOSSIBLE";
}

int main() {
  int tc=gi();
  for(int i=1;i<=tc;i++){
    printf("Case #%d: ",i);
    doit();
    puts("");
  }
  return 0;
}
