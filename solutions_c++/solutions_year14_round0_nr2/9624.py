#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp make_pair                    
#define go(i,n) for(int i=0;i<n;i++)
#define go3(i,j,n) for(int i=j;i<n;i++)

void oku(){

 queue<double> q;

 int T;
 scanf("%d",&T);
 double C,F,X;

 go(cs,T){
  
  cin>>C>>F>>X;


  double best = X / 2.0; 
  double soFar = 0;


  for(int i=0;i<10000;i++){
    double spent = C / (2.0 + i*F);
    soFar+=spent;
    if(best > soFar + X / (2.0 + (i+1)*F))
     best = soFar + X / (2.0 + (i+1)*F);
    else break;
  }

  printf("Case #%d: %.9f\n",cs+1,best);
 
 }

 



}

int main(){
#ifndef ONLINE_JUDGE
freopen("in","r",stdin);
#endif

oku();

return 0;}