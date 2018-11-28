#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<cmath>
#include<stdio.h>

#define MAXNUM 10000000
#define ll long long

using namespace std;

vector<int>numbers;

ll A,B;

int rev( int num ) {
    int sol = 0;
    while ( num > 0 ) {
        sol = ( sol * 10 ) + ( num % 10 );
        num /= 10;
    }
    return sol;
}

bool pal( ll num ) {
    int revised = rev( num );
    if ( revised == num ) {
        return true;
    }
    return false;
}

void Precompute() {
	for (int i=1;i<=MAXNUM;i++) {
		if (pal(i)&&pal(i*i)) {
			numbers.push_back(i*i);
		}
	}
}

void Read() {
	scanf("%lld %lld",&A,&B);
}

int Lower(ll B) {
	int lo=0,hi=numbers.size();
	
	while (lo<hi) {
		int mid=(lo+hi+1)/2;
		
		if (numbers[mid]>B) {
			hi=mid-1;
		}
		else {
			lo=mid;
		}
	}
	
	return lo;
}

int Upper(ll A) {
	int lo=0,hi=numbers.size();
	
	while(lo<hi) {
		int mid=(lo+hi)/2;
		
		if (numbers[mid]>=A)
			hi=mid;
		else
			lo=mid+1;
	}
	
	return lo;
}

void Solve(int kase) {
	printf("Case #%d: %d\n",kase,Lower(B)-Upper(A)+1);
}

int main () {
	freopen("codejam.in","r",stdin);
	freopen("codejam.out","w",stdout);
	
	int t;
	scanf("%d",&t);
	
	Precompute();
	//printf("ok\n");
	
	
	for (int i=1;i<=t;i++) {
		Read();
		Solve(i);
	}
	
}
