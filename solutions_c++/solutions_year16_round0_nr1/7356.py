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
#define ll long long

using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    map<int ,int> m;
    ll x , p ;
    scanf("%I64d",&x);
    int cnt = 0 ;
    for(int i = 1 ; i <= 500 ;i++){
    	p = x*i ;
    	ll tmp = p;
    	while(tmp){
    		if(!m[tmp%10] ){
    			m[tmp%10] = 1;
    			cnt++;
			}
			tmp /= 10;
		}
		if(cnt >= 10)  break;
	}
	if(cnt < 10)   printf("INSOMNIA\n");
	else           printf("%I64d\n",p);
    m.clear();
  }
  return 0;
}
