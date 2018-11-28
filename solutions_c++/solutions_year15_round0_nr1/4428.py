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
	int n;
	char s[1011];
	scanf("%d%s",&n,s);
	int ans=0; 
	int ln=strlen(s),a=0,as=0;
	for(int i=0;i<ln;i++){
		if((a=s[i]-'0')==0)continue;
		if(i>as){
			ans+=i-as;
			as+=i-as;
		}
		as+=a;
	} 
	printf("%d\n",ans);
	return 0;
}

int main(){
	
	freopen("R:\\in","r",stdin);
	freopen("R:\\out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		//printf("Case #%d: %f\n",solvea());
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}