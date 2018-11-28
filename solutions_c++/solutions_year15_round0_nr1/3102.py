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
typedef long double ld;
using namespace std;

int T,S;
char buf[10000];

int main(){
  scanf("%d", &T);
  For(t,T){
    scanf("%d %s", &S, buf);
    int res = 0;
    int lud = 0;
    For(i,S+1){
      int poc = buf[i]-'0';
      if(lud >= i) lud += poc;
      else{
        res += i-lud;
        lud = i+poc;
      }
    }
    printf("Case #%d: %d\n",t+1,res);
  }
  return 0;
}