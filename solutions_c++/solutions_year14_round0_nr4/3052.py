#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
int n, T;
double a[2222], b[2222];

void doit(){
 	sort(a,a+n);
 	sort(b,b+n);
	int j = n - 1, ct = n;
	for (int i = n - 1; i >= 0; i--){
		while (j >= 0 && b[j] > a[i]){
			ct--;
			j--;
		}
		if (j >= 0)
			j--;
	}
	printf("%d ", ct);
}

void doit2(){
	int j = 0, ct = n;
	for (int  i = 0; i < n; i++){
		while (j < n && b[j] < a[i])
			j++;
		if (j < n){
			ct--;
			j++;
		}
	}
	printf("%d\n", ct);
}

int main(){
 	 freopen("D0.in","r",stdin);
 	 freopen("D0.out","w",stdout);
	cin>>T;
	for (int cs = 1; cs <= T; cs ++){
		cin>>n;
		for (int i = 0; i < n; i++)
			cin>>a[i];
		for (int i = 0; i < n; i++)
			cin>>b[i];	
		printf("Case #%d: ", cs);
		doit();
		doit2();
	}
	return 0;
}
