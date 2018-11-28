#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

int main() {
  freopen("in.in", "r", stdin);
  freopen("out", "w", stdout);
  long tt,ans,s,a[2000],c;

long t=0;cin>>t;
 
  char st;
  for (int qq=1;qq<=t;qq++) {
    printf("Case #%d: ", qq);
cin>>s;
    
	for (int i = 0; i <=s; i++){cin>>st;a[i]=st-'0';}
    
	c=0;ans=0;
	for (int i = 0; i <=s; i++){if(a[i])if(c<i){ans+=i-c;c=i;} c+=a[i];}
	
printf("%d\n",ans);  }

  return 0;
}

