#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000+10;

int a[MAXN];

void main2(){
	int n; scanf("%d", &n);
	for (int i=0; i<n; i++)
		scanf("%d", &a[i]);
	for (int i=1; i<=MAXN; i++){
		for (int sp=0; sp<=min(i-1,100); sp++){
			int need = 0;
			for (int j=0; j<n; j++)
				need+= (a[j]+i-sp-1)/(i-sp) - 1;
			if (need <= sp){
				printf("%d\n", i);
				return;
			}

		}
	}
}

int main(){
	int t; scanf("%d", &t);
	for (int o=1; o<=t; o++){
		printf("Case #%d: ", o); 
		main2();
	}
	return 0;
}
