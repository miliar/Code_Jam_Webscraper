#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=22;
const int maxt=2097152;
int n;
int mask;
char str[maxn];
bool v[maxt];
double F[maxt];

void init(){
	scanf("%s",str);
	n=strlen(str);
	mask=0;
	for (int i=0;i<n;i++){
		if (str[i]=='X'){
			continue;
		}
		mask|=(1<<i);
	}
	memset(v,false,sizeof(v));
	memset(F,0,sizeof(F));
	return;
}

double f(int stat){
	if (v[stat]){
		return F[stat];
	}
	v[stat]=true;
	if (stat==0){
		F[stat]=0;
		return 0;
	}
	double ans=0;
	for (int i=0;i<n;i++){
		int cur=i;
		int pos=0;
		while (true){
			if ((1<<cur)&stat){
				break;
			}
			cur++;
			cur%=n;
			pos++;
		}
		ans+=((double)n)+f(stat^(1<<cur))-((double)pos);
	}
	F[stat]=ans/((double)n);
	return F[stat];
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
        printf("Case #%d: %.10lf\n",i,f(mask));
	}
	return 0;
}
