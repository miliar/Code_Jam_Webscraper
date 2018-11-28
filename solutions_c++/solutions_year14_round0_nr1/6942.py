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
#include <cstring>
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define inf 2000000005
#define mod 1000000007
#define ll long long int 
#define PI 3.1415926535897932384626433832795
#define one(mask,i) ((mask>>i)&1)
#define FILENAME ""
using namespace std;
int t,n,m,a[20],b[20],cnt,ans,x,ot;
int main(){
//	freopen(FILENAME".in","r",stdin);
//	freopen(FILENAME".out","w",stdout);
	scanf("%d",&t);
	ot = t;
	while(t){
	
	for(int i=1;i<=20;i++)a[i] = b[i] = 0;
	cnt = 0;
	scanf("%d",&n);
	for(int i=1;i<=4;i++){
		for(int j=1;j<=4;j++){
			scanf("%d",&x);
			if(i == n)a[x] = 1;
		}
	}
	scanf("%d",&m);
	for(int i=1;i<=4;i++){
		for(int j=1;j<=4;j++){
			scanf("%d",&x);
			if(i == m)b[x] = 1;
		}
	}
	printf("Case #%d: ",ot - t + 1);
	for(int i=1;i<=16;i++){
		if(a[i] && b[i])cnt++, ans = i;
	}
	if(cnt > 1)
		printf("Bad magician!");
	else if(cnt == 1){
		printf("%d",ans);
	}
	else 
		printf("Volunteer cheated!");

	if(t != 1)printf("\n");
	t--;
	}
	return 0;
}







