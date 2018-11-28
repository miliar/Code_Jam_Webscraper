#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

int main ()
{
	int no_testcases;
	scanf("%d", &no_testcases);
	
	
	for (int i=0; i<no_testcases; i++) {
		
		long long r,t;
		scanf("%lld",&r);
		scanf("%lld",&t);
		
		//long long temp = 1 - 2*r + sqrt(4*r*r - 4*r +1 + 8*t);
//		temp /= 8;
		long long ans = 1;
		long long exp = 2*ans*ans + (2*r-1)*ans-t;
		while (exp <= 0) {
			ans++;
			exp = 2*ans*ans + (2*r-1)*ans-t;
		}
		
		printf("Case #%d: %lld\n",i+1,ans-1);
		
		
	}
	
	return 0;
}



//class comparenodes{
//public:
//	bool operator() (node* lhs, node* rhs)
//	{
//		return lhs->no_nbs > rhs->no_nbs;
//	}
//};  
////  min no_nbs on top