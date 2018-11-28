#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <tuple>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
 
int solve(){
	int n,a[1011];
	scanf("%d",&n);
	long long ans=0,mx=0; 
	for(int i=0;i<n;i++){ 
		scanf("%d",&a[i]);
	}
	for(int i=1;i<n;i++){
	 	if(a[i-1]>a[i]){
	 		ans+=a[i-1]-a[i];
	 		if(a[i-1]-a[i]>mx)mx=a[i-1]-a[i];
	 	}
	} 
	long long ans2=0;
	 
	/*if(n==2){
		if(a[0]>a[1]){
			ans2=a[0]-a[1];
		}
	}*/
	for(int i=1;i<n;i++){
		if(a[i-1]-mx>=0)ans2+=mx;
		else{
			ans2+=a[i-1];
		}
	}
	
	printf("%I64d %I64d\n",ans,ans2);
	return 0;
}

int main(){
	
	freopen("R:\\a.in","r",stdin);
	freopen("R:\\a.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		//printf("Case #%d: %f\n",solvea());
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}