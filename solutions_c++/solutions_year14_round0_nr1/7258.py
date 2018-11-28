#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;

int main()
{

	int t;
	int m;
	int n;
	int ii = 1;
	int l;
	int k;
	int freq[17];
	scanf("%d",&t);
	while(t--) {
		m = 2;
		int two = 0;
		for(int j = 0 ; j < 17; j++) {
			freq[j] = 0;
		}
		while(m--) {
			scanf("%d",&n);
			for(int i = 0 ; i < 4; i++) {
				for(int j = 0 ; j < 4; j++) {
					scanf("%d",&l);
					if(i+1 == n) {
						freq[l]++;
					}
				}
			}
				
		}
		for(int j = 0 ; j < 17; j++) {
			if(freq[j] == 2) {
				two++;
				k = j;		
			}	
		}
		if(two == 1) {
			printf("Case #%d: %d\n",ii,k);
		}else if(two > 1) {
			printf("Case #%d: Bad magician!\n",ii);
		}else if(two < 1) {
			printf("Case #%d: Volunteer cheated!\n",ii);
		}
		ii++;
	}
	return 0;
}

			


