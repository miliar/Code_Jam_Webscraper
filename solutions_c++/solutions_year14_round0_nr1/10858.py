#include "stack"
#include "cmath"
#include "cstdio"
#include "cstring"
#include "vector"
#include "algorithm"
#include <iostream>
#include <string>
#include <sstream>

using namespace::std;
typedef unsigned long long    u64;
typedef long long    			 i64;

int compare(const void *ap, const void *bp)
{
    const int *a = (int *) ap;
    const int *b = (int *) bp;
    if(*a < *b)
        return -1;
    else if(*a > *b)
        return 1;
    else
        return 0;
}

template <class T>
int row_intersection(T R1, T R2, int n) {
	int element = 0, nb = 0;
	
	sort(R2, R2 + n);
	
	for (int i = 0; i < n; i++) {
		if (bsearch(&R1[i], R2, n, sizeof(R1[0]), compare)) {
			nb++;
			element = R1[i];
		}
	}		
	return (nb > 1) ? -1 : element;
}


int main() {
	const int n = 4;
	int grid1[n][n];
	int grid2[n][n];
	
	int Ti = 0, N, C1, C2;
	
	cin >> N;
	
	while (++Ti <= N) {
		printf("Case #%d: ", Ti);
		
		scanf("%d", &C1);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				scanf("%d", &grid1[i][j]);
		
				
		scanf("%d", &C2);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				scanf("%d", &grid2[i][j]);
		
		C1 -= 1;
		C2 -= 1;		
		
		int intersect = row_intersection(grid1[C1], grid2[C2], n);
		
		if (intersect == -1)
			cout << "Bad magician!";
		else if (intersect == 0)
			cout << "Volunteer cheated!";
		else
			cout << intersect;
		
		cout << endl;
	}
	return 0;
}
