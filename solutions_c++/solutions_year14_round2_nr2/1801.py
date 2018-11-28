#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <stdio.h>
#include <limits.h>
using namespace std;
typedef long long l;
#define mod 1000000007
int main(){
	int t,c=1;
	scanf("%d",&t);
	while(t--){
		int a,b,k;
		scanf("%d %d %d",&a,&b,&k);
		int ans=0;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
		//		printf("i and j are and i xor j is%d %d %d\n",i,j,i&j);
				if((i&j) <k)ans++;
			}
		}
		printf("Case #%d: %d\n",c,ans);
		c++;
	}
	return 0;
}

