#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

double a[2000];
double b[2000];
int t,n;

int main(){
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d",&t);
	for ( int i = 1; i <= t; ++ i){
		printf("Case #%d: ",i);
		scanf("%d",&n);
		for ( int j = 0; j < n; ++ j){
			scanf("%lf",&a[j]);
		}
		for ( int j = 0; j < n; ++ j){
			scanf("%lf",&b[j]);
		}
		sort(a,a+n);
		sort(b,b+n);
		int point = 0;
		int head = 0;
		int tail = n-1;
		int tmp = n;
		for ( int j = 0; j < n; ++ j){
			while (head < n && a[head] < b[j]) ++ head;
			if (head - j > point) point = head - j;
		}
		printf("%d ",n-point);
		point = 0;
		for ( int j = n-1; j >= 0; -- j){
			if (a[j] < b[tail]){
				tail --;
			}
			else{
				++ point;
			}
		}
		printf("%d\n",point);
	}
}