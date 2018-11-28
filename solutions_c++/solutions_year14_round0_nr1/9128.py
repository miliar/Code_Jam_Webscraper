#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;
 
#define N  128
#define ALL(x)     x.begin(),x.end()
#define CLR(x,a)   memset(x,a,sizeof(x))
typedef long long    ll;
const int INF  = 0x3fffffff;
const int MOD  = 1000000007;
/*-----------code------------*/

vector<int> solve(int row){
	row--;
	int a;
	vector<int> v;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			scanf("%d",&a);
			if(i==row) v.push_back(a);
		}
	}
	return v;
}

int check(vector<int> &a,vector<int>&b){
	int cnt=0,ans;
	for(int i=0;i<a.size();i++){
		for(int j=0;j<b.size();j++){
			if(a[i]==b[j]) cnt++, ans=a[i];
		}
	}
	if(cnt==0) return -2;
   	if(cnt>1) return -1;
	return ans;	
}

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int re,Case=1;
	scanf("%d",&re);
	while(re--){
		int row;
		scanf("%d",&row);
		vector<int> a=solve(row);
		scanf("%d",&row);
		vector<int> b=solve(row);
		int op=check(a,b);
		printf("Case #%d: ",Case++);
		if(op==-1) printf("Bad magician!\n");
		else if(op==-2) puts("Volunteer cheated!");
		else printf("%d\n",op);
	}
	return 0;
}
