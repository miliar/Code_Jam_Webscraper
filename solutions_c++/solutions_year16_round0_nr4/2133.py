#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <fstream>
#include <streambuf>

using namespace std;

int main(){

	int t;
	scanf("%d",&t);
	int c = 1;
	while(t--){
		printf("Case #%d:",c++);
		long long k, c, s;
		scanf("%lld %lld %lld",&k,&c,&s);
		for(int i = 1;i<=s;i++)
			printf(" %d",i);
		printf("\n");

	}
	return 0;
}