#include <stdio.h>
#include <string.h>


typedef struct {
	int index, size, sum;
} ITEM;

typedef struct {
	ITEM list[101];
	int count;
} CHECK;

ITEM queue[10001];
CHECK check[2700];

int main() {
	int t;
	scanf("%d", &t);

	for(int i = 0; i < t; i++) {
		for(int j = 0; j < 2700; j++) {
			check[j].count = 0;
		}
		char str[102];
		int n, tail = 0, head = 0;
		scanf("%s %d", &str, &n);

		int len = strlen(str);

		for(int j = 0; j <= len-n; j++) {
			bool flag = false;
			int sum = 0;
			for(int k = j; k < j+n; k++) {
				switch(str[k]) {
				case 'a' :
				case 'e' :
				case 'i' :
				case 'o' :
				case 'u' :
					flag = false;
					break;
				default :
					flag = true;
					break;
				}

				if(!flag) {
					break;
				}

				sum += (str[k]-'a');
			}

			if(flag) {
				int k = 0;
				for(k = 0; k < check[sum].count; k++) {
					if(check[sum].list[k].size == n && check[sum].list[k].index == j) {
						break;
					}
				}

				if(k == check[sum].count) {
					queue[head].index = j;
					queue[head].sum = sum;
					queue[head++].size = n;

					check[sum].list[check[sum].count].index = j;
					check[sum].list[check[sum].count].sum = sum;
					check[sum].list[check[sum].count++].size = n;
				}
			}
		}

		while(tail < head) {
			if(queue[tail].index-1 >= 0) {
				int index, size, sum;

				index = queue[tail].index-1;
				size = queue[tail].size+1;
				sum = queue[tail].sum + (str[queue[tail].index-1] - 'a');

				int k = 0;
				for(k = 0; k < check[sum].count; k++) {
					if(check[sum].list[k].index == index && check[sum].list[k].size == size) {
						break;
					}
				}

				if(k == check[sum].count) {
					queue[head].index = index;
					queue[head].sum = sum;
					queue[head++].size = size;

					check[sum].list[check[sum].count].index = index;
					check[sum].list[check[sum].count].sum = sum;
					check[sum].list[check[sum].count++].size = size;
				}
			}

			if(queue[tail].index+queue[tail].size < len) {
				int index, size, sum;

				index = queue[tail].index;
				size = queue[tail].size + 1;
				sum = queue[tail].sum + (str[queue[tail].index+queue[tail].size] - 'a');

				int k = 0;
				for(k = 0; k < check[sum].count; k++) {
					if(check[sum].list[k].index == index && check[sum].list[k].size == size) {
						break;
					}
				}

				if(k == check[sum].count) {
					queue[head].index = index;
					queue[head].sum = sum;
					queue[head++].size = size;

					check[sum].list[check[sum].count].index = index;
					check[sum].list[check[sum].count].sum = sum;
					check[sum].list[check[sum].count++].size = size;
				}
			}
			tail++;
		}

		printf("Case #%d: %d\n", i+1, head);
	}

	return 0;
}