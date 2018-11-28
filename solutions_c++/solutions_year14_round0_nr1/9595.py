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

  int T;
  cin>>T;

  go(cs,T){
   int r,d;
   set<int> s;

   scanf("%d",&r);

   go(i,4) go(j,4) {
     scanf("%d",&d);
     if( i+1 == r)
      s.insert(d);
   }

   scanf("%d",&r);

   int cnt = 0, any;

   go(i,4) go(j,4){
      scanf("%d",&d);
      if(i+1 == r)
       if(present(s,d))
        cnt++, any = d;
   }

   printf("Case #%d: ",cs+1);
   
   if(cnt==1)
    cout<<any;
   else if(cnt > 1)
    cout<<"Bad magician!";
   else
    cout<<"Volunteer cheated!";

    cout<<endl;
    
  }


}

int main(){
#ifndef ONLINE_JUDGE
freopen("in","r",stdin);
#endif

oku();

return 0;}