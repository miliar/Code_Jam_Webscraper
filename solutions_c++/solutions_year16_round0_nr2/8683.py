#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <iostream>
#define INF (1<<30)
using namespace std;

char cake[110];

bool check(){
	int i=-1;
	while(cake[++i])
		if(cake[i]!='+')return false;
	return true;
}

int main(){
	int T=0, C=0;
	scanf("%d", &T);
	while(T--){
		C++;
		scanf("%s", cake);
		int ans=0;
		while(!check()){
			int l=-1, r;
			while(cake[++l]=='+');
			r=l-1;
			while(cake[++r]=='-');
			r=r-1;
			if(l>0)ans+=2;
			else ans+=1;
			for(int i=l; i<=r; i++)
				cake[i]='+';
		}
		printf("Case #%d: %d\n", C, ans);
	}
	return 0;
}

