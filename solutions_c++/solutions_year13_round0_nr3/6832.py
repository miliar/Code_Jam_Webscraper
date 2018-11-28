#include<stdio.h>
#include<iostream>
#include<vector>

using namespace std;

bool Check (int n) {
	vector<int> na;
	int i=0;
	int buf = n;
	while (n !=0) {

		na.push_back(n%10);
		n /= 10;
	}

	for(i=0;i<na.size()/2;i++) {
		if(na[i]!= na[na.size()-i-1]) return false;
	}
	return true;
}

int Search (int a, int b) {
	int i;
	int min;
	for(i=1; ;i++ ) {

		if(i*i >= a) {
			min = i;
			break;
		}
	}
	int count = 0;
	for(i=min;(i*i)<=b;i++) {
		if(Check(i)) if(Check(i*i)) count++;
	}
	return count;
}

int main(){
	int i;
	int n;
	vector<int> w;
	vector<int> e;
	scanf("%d",&n);
	int a, b;

	for(i=0;i<n;i++) {
		scanf("%d %d",&a,&b);
		w.push_back(a);
		e.push_back(b);
	}
	for(i=0;i<n;i++)printf("Case #%d: %d \n",i+1,Search(w[i],e[i]));



	return 0;
}
