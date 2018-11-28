/*
Author: 1412kid1412@UESTC
*/

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

const int N=10010;
int a[N];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	int test;
	scanf("%d",&test);
	int ct=0;
	while(test--){
		int n,x;
		scanf("%d%d",&n,&x);
		
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		sort(a,a+n);
		
		int lo=0,hi=n-1;
		int ret=0;
		while(lo<hi){
			if(a[lo]+a[hi]<=x){
				lo++;
				hi--;
			}
			else{
				hi--;
			}
			ret++;
		}
		if(lo==hi){
			ret++;
		}
		printf("Case #%d: %d\n",++ct,ret);
	}
	
	return 0;
}