#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int disks[200000];int cmp(const void *a, const void *b) {	int v1 = *((int *)a);	int v2 = *((int *)b);	if (v1 > v2)		return 1;	else if (v1 < v2)		return -1;	return 0;}
void run() {
	int n, size;	int used = 0;	scanf("%d", &n);	scanf("%d", &size);		for (int i = 0; i < n; ++i) {		scanf("%d", &disks[i]);	}	qsort(disks, n, sizeof(disks[0]), cmp);	int left = 0;	int right = n - 1;	while (left < right) {		if (disks[left] + disks[right] > size) {//					printf("%d ", disks[right]);			right--;			used++;		}		else {//			printf("(%d %d) ", disks[left], disks[right]);			used++;			left++;			right--;		}	}	if (left == right)		used++;	printf("%d\n", used);}

int main() {
    int num_cases;
    scanf("%d", &num_cases);
    for (int t = 1; t <= num_cases; ++t) {
        printf("Case #%d: ", t);
        run();
    }
    return 0;
}

