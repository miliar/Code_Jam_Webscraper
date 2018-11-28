#include<stdio.h>
#include<string>

int main()
{
	int N, J;
	scanf("%d", &N);
	scanf("%d%d", &N, &J);
	printf("Case #1:\n");
	unsigned int b = (1U<<(N-1)) + 1;
	int c = 0;
	for (unsigned int i=b;; i+=2) {
		if (i%3 == 0) {
			int d = 0;
			for (unsigned int j=(1U<<(N-1)); j>0; j>>=1) {
				if (i&j) {
					d = 1-d;
				} else {
					d = -d;
				}
			}
			if (d != 0) {
				continue;
			}
			std::string str;
			for (unsigned int j=i; j>0; j>>=1) {
				if (j&1) {
					str = "1" + str;
				} else {
					str = "0" + str;
				}
			}
			printf("%s 3 4 5 6 7 8 9 10 11\n", str.c_str());
			c++;
			if (c == J) {
				break;
			}
		}
	}
	return 0;
}