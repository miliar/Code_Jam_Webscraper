/*
 * A.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: root
 */
#include<bits/stdc++.h>
using namespace std;

#define R(Name) freopen(Name,"r",stdin);
#define W(Name) freopen(Name,"w",stdout);

bitset<10> bits;
void mark(long long n){
	while(n){
		bits[n%10] = 1;
		n/=10;
	}
}

int main(){
	R("input.txt");
	W("output.txt");
	int t,n,cn=0;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		cn++;
		printf("Case #%d: ",cn);
		long long tmp = n;
		bits &= 0;
		for(int it=1;it<1000000;it++){
			mark(tmp*it);
			if(bits.count() == 10){
				printf("%lld\n", tmp*it);
				goto out;
			}
		}
		puts("INSOMNIA");
		out:;
	}
}


