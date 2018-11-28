#include <stdio.h>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;

#define long long long
#define f1(i,n) for (int i=1; i<=n; i++)
#define f0(i,n) for (int i=0; i<n; i++)

set<int> Set;

main(){
	int k, x, t, T, Count, Dcs;
	scanf("%d", &T);
f1(t,T) {
	Set.clear(); Count=0;
	scanf("%d", &k);
	f1(i,4) f1(j,4) {
		scanf("%d", &x);
		if (i==k) Set.insert(x);
	}
	scanf("%d", &k);
	f1(i,4) f1(j,4) {
		scanf("%d", &x);
		if (i==k) if (Set.count(x)) Count++, Dcs=x;
	}
	if (Count==1) 
		printf("Case #%d: %d\n", t, Dcs);
	else if (Count==0)
		printf("Case #%d: Volunteer cheated!\n", t);
	else 
		printf("Case #%d: Bad magician!\n", t);		
}
}
