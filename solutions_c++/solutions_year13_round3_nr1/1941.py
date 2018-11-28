#include <cstdio>
#include <omp.h>
#include <stdlib.h>
#include <map>
#include <cstring>

using namespace std;

int counter = 0;

bool isConsonant(char c) {
	return !(c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o');
}

void make() {
	char name[100]; 
	memset(name, 0, 100);
	
	int n;

	scanf("%s %d", &name, &n);

	int i = 0;
	int result = 0;
	bool isOk = true;
	while(name[i + n - 1] != 0) {
		i++;
	}

	int length = i + n;
	for(int k = n; k < length; k++) {
		char substr[100];
		memset(substr, 0, 100);

		for(int l = 0; l + k < length; l++) {
			memcpy(substr, name + l, k) ;
			//printf("substr[%d]:%s\n", k, substr);
			
			i = 0;
			while(substr[i + n - 1] != 0) {
				for(int j = i; j < i+n; j++) {
					//printf("checked[%d]:%c\n", j, substr[j]);
					isOk = isConsonant(substr[j]);
					if(!isOk)
						break;
				}
				if(isOk) {
					result++;
					//printf(" accepted\n");
					break;
				}
				else {
					//printf(" rejected\n");
				}
				isOk = true;
				i++;
			}
		
		}
	}

	printf("Case #%d: %d\n", ++counter, result);

	/*
	long long n = 0;
	while(t > 0) {
		t -= (r << 1) + 1;
		if(t >= 0)
			n++;

		r += 2;
	}

	printf("Case #%d: %lld\n", ++counter, n);
	*/
}

int main() {
	int nthreads, tid;
	
	/* Fork a team of threads giving them their own copies of variables */
	int t; scanf("%d", &t);
	//#pragma omp parallel private(nthreads, tid)
	//{
		while(t-- > 0) {
			/* Obtain thread number */
			//tid = omp_get_thread_num();
			//printf("Hello World from thread = %d\n", tid);

			make();
		}
	//}  /* All threads join master thread and disband */

	return 0;
}
