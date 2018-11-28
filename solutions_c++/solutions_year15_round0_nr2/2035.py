#include <bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{
	ll i,j,k,l,t,d,m,mid,low,high,time,val;

	scanf("%lld", &t);

	for(i=1;i<=t;i++) {
		scanf("%lld", &d);

		ll diner[d];

		m = -1;
		for(j=0;j<d;j++) {
			scanf("%lld", &diner[j]);
			m = max(m,diner[j]);
		}
		time = INT_MAX;

		for(k=1;k<=m;k++) {
			low = 0;

			for(j=0;j<d;j++) {
				low = low + ((ceil(((double)diner[j])/k)) - 1);
			}
			low = low + k;

			if(time > low) {
				time = low;
				val = k;
			}
		}
	//	cout<<val<<endl;
		printf("Case #%lld: %lld\n", i,time);
	
	/*
		low = 1;
		high = m;

		while(low<high) {
			mid = (low+high)/2;

			time = 0;

			for(j=0;j<d;j++) {
				time = time + ((ceil(((double)diner[j])/mid)) - 1);
			}

			if(time + mid < high) {
				high = mid + time;
			} else {
				low = mid + 1;
			}
		}
		
		printf("Case #%lld: %lld\n", i,high);
	*/
	}

	return 0;
}
