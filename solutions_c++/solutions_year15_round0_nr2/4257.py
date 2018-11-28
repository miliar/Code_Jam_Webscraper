#include<iostream>
#include<stdio.h>
using namespace std;


int main() {
	freopen("B-large.in","r",stdin);
	
	int T;
	int K;
	int n;
	int a[1001];
	int result;
	int best;


	cin>>T;
	for (int t=0; t<T; t++) {
		cin>>n;
		for (int i=0; i<n; i++) cin>>a[i];
		best = -1;
		for (K = 1; K<=1000; K++) {
			result = 0;
			for (int i=0; i<n; i++) {
				result = result + (a[i]-1)/K;
			}

			result += K;
			if (best == -1 || result<best) best = result; 
		}
		cout<<"Case #"<<t+1<<": "<<best<<"\n";
	}
}
