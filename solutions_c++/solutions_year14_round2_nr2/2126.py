#include<iostream>
#include<vector>
#include<stack>
#include<cstring>
#include<map>
#include<set>
#include<string>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<sstream>
#include<cmath>
#include<cctype>
#include<fstream>
#include<set>
#define mp(x,y) make_pair(x,y)
using namespace std;

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.in","w",stdout);
	int a,b,k,t;
	scanf("%d",&t);
	for(int u=1;u<=t;++u){
		scanf("%d%d%d",&a,&b,&k);
		int c=0;
		for(int i=0;i<a;++i)
			for(int j=0;j<b;++j)
				if((i&j)<k)
					c++;
		printf("Case #%d: %d\n",u,c);
	}
	return 0;
}

