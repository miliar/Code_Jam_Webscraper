#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

#define CLEAR(X) memset(X,0,sizeof(X))
#define REP(i,n) for(int i=0;i<(n);i++) 
template <class T> vector<T>parse(string s,const char d=' '){
  vector<T> v; string p; s+=d; int i=0; 
  while(i<(int)s.size())
    if (s[i] == d){stringstream u; u<<p; T t; u>>t; v.push_back(t); p=""; while(i<(int)s.size() && s[i]==d)i++;} else p+=s[i++];   
  return v;
} 

typedef long long ll;
typedef long double ld;

int a[2020];
int b[2020];
int n;
int cur[2020];
int ca[2020],cb[2020];
vector<int> sol;

void f() {
  REP(p,n){
    int mr[2020];
    int minr[2020];
    mr[n-1] = 0;
    for (int i=n-2;i>=0;i--)mr[i]=max(mr[i+1],cb[i+1]);
  
    minr[0]=n+2;
    for(int i=1;i<n;i++)
      if(cur[i-1]!=-1)
        minr[i]=minr[i-1];
      else
        minr[i]=min(minr[i-1],b[i-1]);
  
    int minl[2020];
    minl[n-1]=n+2;
    for(int i=n-2;i>=0;i--)
      if(cur[i+1]!=-1)
        minl[i]=minl[i+1];
      else
        minl[i]=min(minl[i+1],a[i+1]);
  
    int ml=0;
    for(int i=0;i<n;i++){
      if (cur[i] == -1 && ml + 1 == a[i] && mr[i]+1 == b[i] && minr[i] > b[i] && minl[i] > a[i]){
        cur[i] = p + 1;
        ca[i] = a[i];
        cb[i] = b[i];
        break;
      }
      ml = max(ml, ca[i]);
    }
  }
  vector<int> c;
  REP(i,n)c.push_back(cur[i]);
  sol=c;
}

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    scanf("%d",&n);
    sol.resize(n);
    REP(i,n)sol[i]=n+10;
    REP(i,n)scanf("%d",&a[i]);
    REP(i,n)scanf("%d",&b[i]);
    REP(i,n)ca[i]=cb[i]=0;
    REP(i,n)cur[i]=-1;
    f();
    REP(i,n)printf(" %d",sol[i]);printf("\n");
  }
  return 0;
}
