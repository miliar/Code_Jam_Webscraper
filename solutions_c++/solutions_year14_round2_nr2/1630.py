//UESTC_L3

#include <stdexcept>
#include <cstdarg>
#include <iostream>
#include <fstream>
#include <exception>
#include <memory>
#include <locale>
#include <sstream>
#include <set>
#include <list>
#include <bitset>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <string>
#include <utility>
#include <cctype>
#include <climits>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <map>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <vector>
#include <queue>
#include <deque>
#include <cstdlib>
#include <stack>
#include <iterator>
#include <functional>
#include <complex>
#include <valarray>
using namespace std;

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	int test;
	scanf("%d",&test);
	int ct=0;
	while(test--){
		int a,b,k;
		scanf("%d%d%d",&a,&b,&k);
		int ret=0;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				if((i&j)<k)ret++;
			}
		}
		printf("Case #%d: %d\n",++ct,ret);
	}
	return 0;
}