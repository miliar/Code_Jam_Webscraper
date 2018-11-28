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

long long cnt = 0;

void update(long long xd){
	if(xd == 0){cnt|=1;return;}
	while(xd>0){
		cnt|=(1<<(xd%10));
		xd/=10;
	}
}


int main(){

	int t;
	scanf("%d",&t);
	int c = 1;
	while(t--){
		cnt = 0;
		printf("Case #%d: ",c++);
		long long n;
		scanf("%lld",&n);
		long long ans = -1;
		for(long long i = 1;ans==-1 && i<1000000;i++){
			long long xd = i*n;
			update(xd);
			if(cnt == ((1<<10)-1))
				ans = xd;
		}
		if(ans == -1)
			printf("INSOMNIA\n");
		else
			printf("%lld\n",ans);
	}
	return 0;
}