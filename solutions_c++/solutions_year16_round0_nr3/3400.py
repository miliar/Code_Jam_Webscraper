#include <algorithm>
#include <bitset>
#include <cstdio>
#include <cstring>
#include <string>

#define MAXN 40
#define MAXJ 510

#define N 16
#define J 50
#define LIMIT 16384

void convert(const char *s, unsigned long long array[11])
{
	int len = strlen(s);

	for(int base = 2; base <= 10; ++base) {
		unsigned long long sum = 0;

		for(int i = 0; i < len; ++i) {
			sum = sum * base + (s[i] - '0');
		}	

		array[base] = sum;
	}
}

unsigned long long isPrime(unsigned long long val)
{
	for(int i = 2; i < val / 2; ++i) {
		if(val % i == 0) {
			return i;
		}
	}

	return 0;
}

int main()
{
	unsigned long long divisor[MAXJ][11];
	std::string sArray[MAXJ];

	int tmp;
	scanf(" %d %d %d", &tmp, &tmp, &tmp);

	for(int k = 0, count = 0; k < LIMIT && count <= J; k += 210) {
		std::string binary = std::bitset<N - 2>(k).to_string();
		binary.insert(0, "1");
		binary.append("1");

		unsigned long long array[11];
		convert(binary.c_str(), array);

		sArray[count] = binary;
		for(int base = 2; base <= 10; ++base) {
			divisor[count][base] = isPrime(array[base]);

			if(divisor[count][base] == 0) {
				break;
			}

			if(base == 10) {
				count++;
			}
		}
	}

	printf("Case #1:\n");
	for(int i = 0; i < J; ++i) {
		printf("%s", sArray[i].c_str());
		for(int base = 2; base <= 10; ++base) {
			printf(" %llu", divisor[i][base]);
		}
		printf("\n");
	}

	return 0;
}
