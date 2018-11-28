#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#define debug(x) cerr << #x << " = " << x << endl;
#define p_case(x) printf("Case #%d: ",x);

#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 10000


int main(){
  int T;

  scanf("%d",&T);

  for(int i=1;i<=T;i++){
    char s[200];
    int n;
    
    scanf("%s",s);
    n = strlen(s);

    bool f = false,f2 = true;
    int t = 0,ans;
    vector<int> vec;
    
    for(int i=0;i<n;i++){
      if(s[i]=='-') f2 = false;
      
      if(f ^ (s[i]=='+')){
	if(t>0)vec.push_back(t);
	t = 1;
	f = !f;
      }else{
	t++;
      }
    }

    if(s[n-1]=='-')
      vec.push_back(t);

    ans = (int)vec.size();

    p_case(i);
    printf("%d\n",ans);

  }
  
  return 0;
}
