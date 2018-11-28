#include <bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{
	ll store[9][9] = {
		{0,0,0,0,0,0,0,0,0},
		{0,1,2,3,4,5,6,7,8},
		{0,2,5,4,7,6,1,8,3},
		{0,3,8,5,2,7,4,1,6},
		{0,4,3,6,5,8,7,2,1},
		{0,5,6,7,8,1,2,3,4},
		{0,6,1,8,3,2,5,4,7},
		{0,7,4,1,6,3,8,5,2},
		{0,8,7,2,1,4,3,6,5}
	};

	ll i,j,k,l,x,t,req,cur,lim;

	char str[100000];
	ll arr[100000];

	scanf("%lld", &t);

	for(k=1;k<=t;k++) {
		scanf("%lld%lld", &l,&x);
		scanf(" %s", str);

		lim = l*x;

		for(i=1;i<=lim;i++) {
			if(str[(i-1)%l]=='i') arr[i] = 2;
			else if(str[(i-1)%l]=='j') arr[i] = 3;
			else if(str[(i-1)%l]=='k') arr[i] = 4;
		}

//		for(i=1;i<=lim;i++) cout<<arr[i]<<" ";
//		cout<<endl;

		req = 2;
		cur = 1;
		
		i = 1;
		while((req<=4) && (i<=lim)) {
			if(store[cur][arr[i]]==req) {
				req++;
				i++;
				cur = 1;
			} else {
				cur = store[cur][arr[i]];
				i++;
			}
		}

		if(req>4) {
			if(i>lim) printf("Case #%lld: YES\n", k);
			else if(i<=lim) {
				cur = 1;
				while(i<=lim) {
					cur = store[cur][arr[i]];
					i++;
				}
				if(cur==1) {
					printf("Case #%lld: YES\n", k);
				} else {
					printf("Case #%lld: NO\n", k);
				}
			}
		} else if(i>lim) {
			printf("Case #%lld: NO\n", k);
		}
	}

	return 0;
}
