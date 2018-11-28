#include "akash.h"

// global
int junk[4]; int *ptr;
char buf[1024];

inline void makeArr(int *arr) {
	static int row_no;
	scanf("%d", &row_no);
	for (int i = 1; i <= 4; ++i) {
		if (i == row_no) ptr = arr;
		else ptr = junk;
		scanf("%d %d %d %d", &ptr[0],&ptr[1],&ptr[2],&ptr[3]);
	}
}
void pr(bool *arr) {
	for (int i = 0; i < 4; ++i)
		printf("%d ", arr[i]);
	printf("\n");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int arr1[4],arr2[4]; int twice, last;
	int no_of_cases; scanf("%d", &no_of_cases);
	for (int case_no = 1; case_no <= no_of_cases; ++case_no) {
		makeArr(arr1); makeArr(arr2); twice = 0; last = 0;

		bool map[17]; memset (map,false,17); FOR(i,0,4) map[arr1[i]] = true;
		FOR(i,0,4) if (map[arr2[i]]) { twice++; last = arr2[i]; }
		switch(twice) {
			case 0: sprintf(buf, "Volunteer cheated!"); break;
			case 1: sprintf(buf, "%d", last); break;
			default: sprintf(buf, "Bad magician!"); break;
		}

		printf("Case #%d: %s\n", case_no,buf);
	}

	return 0;
}
