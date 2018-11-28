#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;


int main() {

	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; ++kase) {

		int a,b,k,count = 0;
		cin >> a >> b >> k;

		for (int i = 0; i < a; ++i)
			for (int j = 0; j < b; ++j) 
				if ((i & j) < k)
					++count;

		printf("Case #%d: %d\n", kase, count);
			

	}

	return 0;
}