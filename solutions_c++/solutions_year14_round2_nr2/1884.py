#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	
	
	int i,j,k,l,t,a,b;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	
	cin >> t;
	
	
	long long int answer;
	int s;
	
	for(i = 1; i <= t; i++) {
		scanf("%d", &a);
		scanf("%d", &b);
		scanf("%d", &k);
		
		answer = 0;
		
		for(s = 0; s < a; s++) {
			for(j = 0; j < b; j++){
				if ((s & j) < k){
					answer++;
				}
			}
		}
		
		printf("Case #%d: %lld\n",i,answer);
	}

	return 0;
}
