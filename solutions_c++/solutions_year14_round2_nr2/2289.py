#include <string>
#include <vector>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<functional>
//--
#include<list>
#include<deque>
#include<bitset>
#include<set>
#include<map>
#include<cstdio>
#include<cstring>
#include<sstream>
#define X first
#define Y second
#define pb push_back
#define pqPair priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > >
#define all(X) (X).begin(),(X).end()

using namespace std;
typedef __int64 ll;

int main(){
  int t,T;
  cin>>T;
  for(t=1;t<=T;t++){
    int i,j,k,A,B,K;
    ll re=0;
    cin>>A>>B>>K;
//    cout<<A<<B<<K;
    for(i=0;i<A;i++){
      for(j=0;j<B;j++){
        if((i&j)<K){
          re++;
        //  cout<<i<<","<<j<<endl;
        }
      }
    }
    cout<<"Case #"<<t<<": "<<re<<endl;
  }
  return 0;
}