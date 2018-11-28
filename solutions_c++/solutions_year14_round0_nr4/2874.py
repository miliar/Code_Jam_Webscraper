#include<vector>
#include<iostream>
#include<stdio.h>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<climits>
#include<sstream>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>
 
#define FL(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) for(int i=0;i<n;i++)
#define SORTF(x) sort(x.begin(),x.end(),func);
#define SORT(x) sort(x.begin(),x.end())
#define pb(x) push_back(x)
#define ll long long
#define SET(v, val) memset(v, val, sizeof(v)) ;
#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
#define ALL(v) v.begin(),v.end()
#define REVERSE(v) { reverse(ALL(v)) ; }
#define UNIQUE(v) unique((v).begin(), (v).end())
#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }
#define fill(x,n) memset(x,n,sizeof(x))
#define si(x) scanf("%d",&x)
#define si2(x,y) scanf("%d %d",&x,&y)
#define si3(x,y,z) scanf("%d %d %d",&x,&y,&z)
 
#define ss(x) scanf("%s",x)
 
#define sc(x) scanf("%c",&x)
 
#define sf(x) scanf("%f",&x)
 
#define sl(x) scanf("%lld",&x)
#define sl2(x,y) scanf("%lld %lld",&x,&y)
#define sl3(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
 
#define ll long long
#define str string
#define lli long long int
#define ch char
#define fl float
  
#define printi(x) printf("%lld\n",x)
#define printi2(x,y) printf("%lld %lld\n",x,y)
#define printi3(x,y,z) printf("%lld %lld %lld\n",x,y,z)
#define prints(x) printf("%s\n",x)

//#define size(A) ((int)A.size())
#define len(A) ((int)A.length())
#define mp(A,B) make_pair(A,B)

using namespace std;

int main()
{
  int n;
  scanf("%d",&n);
  for(int t=1;t<=n;t++) {
    int N;
    scanf("%d",&N);
    double val;
    list<double> listN1;
    list<double> listK1;

    for(int i=0;i<N;i++) {
      scanf("%lf",&val);
      listN1.push_back(val);
    }
    for(int i=0;i<N;i++) {
      scanf("%lf",&val);
      listK1.push_back(val);
    }
    
    listN1.sort();
    listK1.sort();
    
    list<double> listN2(listN1);
    list<double> listK2(listK1);
    
  double x,y;
    for(int i=0;i<listK1.size();i++) {
  //  while(listN2.begin()!=listN2.end()) {
      x=listK1.front();
    //  printf("here %lf\n",x);
      int flag=0;
	//for(int j=0;j<listK2.size();j++) {
	 // y=listK2.at(j);
      int j=0;
      for (list<double>::iterator it = listN1.begin(); it != listN1.end(); it++) {
	  y=*it;
	if(y>x) {
	  flag=1;
	  list<double>::iterator listN1_iter=listN1.begin();
	  list<double>::iterator listK1_iter=listK1.begin();
	  advance(listN1_iter,j);
	  advance(listK1_iter,i);
	  listK2.erase(listN1_iter);
	  listN2.erase(listK1_iter);
	//  printf("coming\n");
	  i--;
	  break;
	}
      j++;
      }
    if(flag==0) {
      break;
    }
    }
  
    for(int i=0;i<listN2.size();i++) {
  //  while(listN2.begin()!=listN2.end()) {
      x=listN2.front();
    //  printf("here %lf\n",x);
      int flag=0;
	//for(int j=0;j<listK2.size();j++) {
	 // y=listK2.at(j);
      int j=0;
      for (list<double>::iterator it = listK2.begin(); it != listK2.end(); it++) {
	  y=*it;
	if(y>x) {
	  flag=1;
	  list<double>::iterator listK2_iter=listK2.begin();
	  list<double>::iterator listN2_iter=listN2.begin();
	  advance(listK2_iter,j);
	  advance(listN2_iter,i);
	  listK2.erase(listK2_iter);
	  listN2.erase(listN2_iter);
	//  printf("coming\n");
	  i--;
	  break;
	}
      j++;
      }
    if(flag==0) {
      break;
    }
    }
    //ans is sizeof(listN)
    printf("Case #%d: ",t);
    printf("%d %d\n",(N-(int)listN1.size()),(int)listN2.size());
   }
  return 0;
} 