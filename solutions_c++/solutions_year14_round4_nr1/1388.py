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
    cout<<"Case #"<<t<<": ";
    int i,j,k,n,m,tmp;
    multiset<int> files;
    multiset<int>::iterator it;
    cin>>n>>m;
    for(i=0;i<n;i++){
      cin>>tmp;
      files.insert(tmp);
    }
    int mx,re=0;
    while(files.size()){
      re++;
      mx=*files.rbegin();
  //    cout<<mx<<",";
      files.erase(files.find(mx));
      if(files.empty())break;
      it=files.upper_bound(m-mx);
      if(it==files.begin())continue;
      it--;
 //     cout<<*it<<endl;
      files.erase(it);
    }
    cout<<re<<endl;
  }
  return 0;
}