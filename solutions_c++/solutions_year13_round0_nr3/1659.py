
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <iostream>
#include <assert.h>



#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define PI 3.14159265358979323
#define EPS 0.000000001
#define INF 1000000000

int T;



bool is_palin(long long a) {
	char num[110];
	int n=0;
	if (a==0) return true;
	
	while (a) {
		num[n++]=a%10;
		a/=10;
	}
	
	for (int i=0;i<n;i++) {
		if (num[i]!=num[n-1-i]) return false;
	}
	
	return true;
}


long long get_half(long long a) {
	char num[110];
	int n=0;
	if (a==0) return true;
	
	while (a) {
		num[n++]=a%10;
		a/=10;
	}
	
	long long ret=0;
	
	
	for (int i=0;i<(n+1)/2;i++) {
		ret*=10;
		ret+=num[i];
	}
	
	return ret;
}

long long polins[500];
int pnum;

int main() {
	int cs=1;
	char tc;
	
	long long brk = 10;
	
	pnum=0;
	
	for (long long i=0;i<30000000;i++) {
		if (i>10&&i%10==3) {
			i+=7;
			continue;
		}


//		if (i==brk) {
//			brk*=10;
//			cout<<endl;
//		}
		
//		if (is_palin(i)&&is_palin(i*i)) {
//			cout<<get_half(i)<<"\t"<<i<<"\t"<<i*i<<endl;
//		}

		if (is_palin(i)&&is_palin(i*i)) {
			polins[pnum++]=i*i;
		}
		
	}
	
	
	
	
	cin>>T;
	while (T-->0) {
		
		long long A, B;
		cin>>A>>B;
		
		int sum=0;
		for (int i=0;i<pnum;i++) {
			if (polins[i]>=A&&polins[i]<=B)  sum++;
		}
		
		printf("Case #%d: %d", cs++, sum);
		
		
		printf("\n");
	}

	
    return 0;
    
}


