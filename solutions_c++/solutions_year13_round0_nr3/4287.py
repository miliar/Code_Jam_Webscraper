#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <queue>

using namespace std;
vector<int> v;

bool palin(long long int a)
{
		v.clear();
		
		while ( a != 0) {
				v.push_back(a % 10);
				a /= 10;
		}

		for (int i = 0; i < v.size()/2; i++) {
				if (v[i] != v[v.size() - 1 - i])
						return false;
		}

		return true;
}

bool arr[10000003];

int main()
{
	int test,   sum = 0;
	long long int A, B, i;
	
	memset(arr, 0, sizeof(arr));

	for (long int i = 1; i < 10000003; i++) {
			if (palin(i) && palin(i*i))
					arr[i] = true;
	}
			

	scanf("%d", &test);
	
	for (int t = 1; t <= test; t++) {

			scanf("%lld%lld", &A, &B);
			sum = 0;			
			for (i = (int) ceil(sqrt(A)) ; i <= (int) floor(sqrt(B)); i++) {
					if (arr[i]) {
							sum++;
					}
			}
			printf("Case #%d: %d\n", t, sum);
	}

	return 0;
}



