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
	int n,m,x;
	scanf("%d%d%d",&x,&n,&m);
	if(x==1){printf("GABRIEL\n");return 0;}
	else if(x==2){
		if(n*m%2==0){printf("GABRIEL\n");}
		else printf("RICHARD\n");
		return 0;
	}
	else if(x==3){
		if(n<3&&m<3||n==1||m==1||n*m%3){printf("RICHARD\n");}
		else{printf("GABRIEL\n");}
		return 0;
	}
	else{
		if(n<4&&m<4||n<3||m<3||n*m%4)printf("RICHARD\n");
		else printf("GABRIEL\n");
		return 0;
	} 
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