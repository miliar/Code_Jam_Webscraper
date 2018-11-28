#include <iostream>
#include <stdio.h>
#include <math.h>
#include <list>
#include <queue>
#include <vector>
#include <functional>
#include <stack>
#include <utility> 
#include <stdlib.h>
#include <map>
#include <string.h>
#include <algorithm>
typedef long long int ll;
#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))
#define gc getchar_unlocked
#define CLR(a) memset(a, 0, sizeof(a))
using namespace std;
int main() {
	int t, arr1[5], arr2[5], ans1, ans2, i, j, a, common, k;
	cin>>t; 
	for(k=1;k<=t;++k) {
		cin>>ans1;
		for(i=1;i<=4;++i) {
			for(j=1;j<=4;++j) {
				cin>>a;
				if(ans1 == i) {
					arr1[j] = a;
				}
			}
		}
		cin>>ans2;
		for(i=1;i<=4;++i) {
			for(j=1;j<=4;++j) {
				cin>>a;
				if(ans2 == i) {
					arr2[j] = a;
				}
			}
		}
		common = 0;
		for(i=1;i<=4;++i) {
			for(j=1;j<=4;++j) {
				if(arr1[i] == arr2[j]) { ++common; a = arr1[i]; }
			}
		}
		if(common == 0) {
			printf("Case #%d: Volunteer cheated!\n", k);
		} else if(common > 1) {
			printf("Case #%d: Bad magician!\n", k);
		} else {
			printf("Case #%d: %d\n", k, a);
		}
	}
	return 0;
}