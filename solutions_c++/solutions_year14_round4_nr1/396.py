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
#include <queue>
#include <memory.h>

using namespace std;

int ans=0,n,m;
int a[10005];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ca=0;
	scanf("%d",&t);
	while(t--){
		ans=0;
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++) scanf("%d",&a[i]);
		sort(a,a+n);
		ans=n;
		int j=n-1;
		for(int i=0;i<n && j>i;i++){
			while(j>i && a[i]+a[j]>m) j--;
			if(j>i){
				ans--;
				j--;
			}
		}
		printf("Case #%d: %d\n",++ca,ans);
	}
	return 0;
}