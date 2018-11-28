#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include <algorithm>
#include <cmath>
#include "time.h"
#include "stdlib.h"
using namespace std;
int main()
{
	int n,i,txt,l=1;
	double c,f,x,ans,y;
	freopen("c:\\B-small-attempt6.in","r",stdin);
	freopen("c:\\B-small-attempt6.out","w",stdout);
	scanf("%d",&txt);
	while(txt--){
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: ",l++);
		y=2.0;
		ans=0;
		while(1){
			if(x/y<=(c/y+x/(y+f))){
				ans+=(x/y);
				break;
			}
			else ans+=(c/y);
			y+=f;
		}
		printf("%.7lf\n",ans);
	}
	return 0;
}
