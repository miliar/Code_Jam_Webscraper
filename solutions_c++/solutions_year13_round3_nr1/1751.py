#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
#include<complex>
#include<numeric>
#include<set>
#include<map>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<utility>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<climits>
#include<cfloat>
#include<cassert>

using namespace std;

typedef long long LL;

bool check(char c){
  return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}
int main(){
  int tc;
  cin>>tc;
  for(int c=1;c<=tc;c++){
    string s;
    int n;
    cin>>s>>n;
    int L=s.size();
    multiset<string> S;
    for(int i=n;i<=L;i++){
      for(int j=0;j<=L-i;j++){
        string tmp=s.substr(j,i);
        //cout<<tmp<<endl;
        int count=0;
        bool flag=false;
        for(int k=0;k<i;k++){
          if(check(tmp[k]))count=0;
          else count++;
          if(count==n){
            flag=true;
            break;
          }
        }
        if(flag){
          //cout<<"OK"<<endl;
          S.insert(tmp);
        }
      }
    }
    int ans=S.size();
    printf("Case #%d: %d\n",c,ans);
  }
  return 0;
}