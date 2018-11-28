#include <iostream>
#include <cstdio>
#include <algorithm>
#define sd(x) scanf("%d",&x)
using namespace std;

double n[1001];
double k[1001];
int main() {
	int t,test = 0;
	sd(t);
	while(t--) {
		test++;
		printf("Case #%d: ",test);
		int nu;
		sd(nu);
		for(int i = 0; i < nu; i++) 
			cin>>n[i];
		for(int i = 0; i < nu; i++) 
			cin>>k[i];
		sort(n, n + nu);
		sort(k ,k + nu);
		int i = 0,j = 0,count = 0;
		while(i<nu && j<nu){
			if(n[i] > k[j]) {
				count++;
				i++;j++;
			} else {
				i++;
			}
		}
		printf("%d ",count);
		count = 0;
		i=0;j=0;
		while(i<nu && j<nu){
			if(k[j] > n[i]) {
				count++;
				i++;j++;
			} else {
				j++;
			}
		}
		printf("%d\n",(nu-count));
	}
	return 0;
}
