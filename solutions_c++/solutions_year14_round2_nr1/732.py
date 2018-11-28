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

int T,N;
vector<vector<int> > V;
string S;
char buf[1000];

vector<int> spracuj(char *c){
  vector<int> A;
  A.pb(1);
  for(int i=1; c[i]; i++)
    if( c[i] == c[i-1] ) A.back()++;
    else A.pb(1);
  return A;
}


int main(){
  scanf(" %d", &T);
  For(t,T){
    scanf(" %d", &N);
    V.clear();
    bool ok = 1;
    
    For(i,N){
      scanf(" %s", buf);
      string s = ""; s+= buf[0];
      Fors(j,buf) if(buf[j] != s[int(s.size())-1]) s+= buf[j];
      if(i==0) S=s;
      else if(S != s){
	printf("Case #%d: Fegla Won\n",t+1);
	ok = 0;
	break;
      }
      //printf("som tu\n");
      V.pb( spracuj(buf) );
    }
    
    if(!ok) continue;
    
    int zmeny=0;
    For(i,V[0].size()){
      int minz=1000000;
      For(o,101){
	int sol = 0;
	For(j,V.size()) sol += round(fabs(o-V[j][i]));
	minz = min(minz, sol);
      }
      zmeny += minz;
    }
    printf("Case #%d: %d\n",t+1,zmeny);
  }
  return 0;
}