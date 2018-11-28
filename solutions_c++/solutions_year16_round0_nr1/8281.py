#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void countVal(long long int i, set<int> &s){
	//int k;
	while(i>9){
		s.insert(i%10);
		i = i/10;
	}
	s.insert(i);
}

int main() {
	// your code goes here
	set<int> s;
	int t, i, n, j, k;
	scanf("%d",&t);
	long long int val;
	int flag;
	//set<int> ::iterator it;
	for(i=1;i<=t;i++){
		scanf("%lld", &val);
		s.clear();
		if(val==0){
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		j = 1;
		flag = 0;
		while(flag!=1){
			countVal((j*val), s);
			for(k=0;k<=9;k++){
				if(s.find(k)==s.end()){
					break;
				}
			}
			if(k==10){
				flag = 1;
			}
			else{
				j++;
			}
		}
		printf("Case #%d: %d\n", i, j*val);
	}
	return 0;
}