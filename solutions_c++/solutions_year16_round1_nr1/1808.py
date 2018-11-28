
#include <iostream>
#include <cstring>

using namespace std;

void insert_start(char* str, int size, char ch);
void insert_end(char* str, int size, char ch);

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		char base_str[1001], sort_str[1002];
		scanf("%s", base_str);
		sort_str[0] = base_str[0];
		sort_str[1] = '\0';
		for(int j = 1; j < strlen(base_str); ++j) {
			if(base_str[j] >= sort_str[0])
				insert_start(sort_str, strlen(sort_str), base_str[j]);
			else
				insert_end(sort_str, strlen(sort_str), base_str[j]);
		}
		printf("Case #%d: %s\n", i, sort_str);
	}

	return 0;
}

void insert_start(char* str, int size, char ch) {
	for(int i = size; i >= 0; --i)
		str[i + 1] = str[i];
	str[0] = ch;
}
void insert_end(char* str, int size, char ch) {
	str[size] = ch;
	str[size + 1] = '\0';
}
