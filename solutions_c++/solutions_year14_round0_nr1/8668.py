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
int a,b,x;
vector<int> V;

int main(){
  scanf(" %d ", &T);
  For(t,T){
    V.clear();
    V.resize(16,0);
    
    scanf(" %d ", &a);
    For(i,16){ scanf(" %d ", &x); if(i/4 == a-1)V[x-1]++;}
    scanf(" %d ", &b);
    For(i,16){ scanf(" %d ", &x); if(i/4 == b-1)V[x-1]++;}
    x=-1;
    For(i,16)
      if(x==-1 && V[i]==2) x=i;
      else if(V[i]==2) x=100;
    if(x==-1)
      printf("Case #%d: Volunteer cheated!\n",t+1);
    else if(x==100)
      printf("Case #%d: Bad magician!\n",t+1);
    else
      printf("Case #%d: %d\n",t+1,x+1);  
  }
  return 0;
}