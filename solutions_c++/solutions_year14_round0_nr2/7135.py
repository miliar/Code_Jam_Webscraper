#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
using namespace std;
#define LL long long
#define Mod (1e9+7)
const int inf = 0x3f3f3f3f;
const int Max = 1010;
const int EP = 1e-6;
int n;
double c,f,x;
int main(){
	int T,Case = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%lf%lf%lf",&c,&f,&x);
		double time;
		time = x/2;
		double tmp = 2,t;
		t = time-(x-c)/tmp+x/(tmp+f);
		while(time > t){
			tmp += f;
			time = t;
			t = t-(x-c)/tmp+x/(tmp+f);
		}
		printf("Case #%d: %.7lf\n",Case++,time);
	}
}
