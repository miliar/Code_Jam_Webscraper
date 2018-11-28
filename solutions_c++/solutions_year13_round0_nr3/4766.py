#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int t,a,b;
int x[5]={1,4,9,121,484};

int main(){
	int h,i,j,k;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d",&a,&b);
		k=0;
		for(j=0;j<5;j++)if(x[j]>=a && x[j]<=b)k++;
		printf("Case #%d: %d\n",h,k);
	}
	return 0;
}
