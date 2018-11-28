#include<cstdio>
#include<cstring>
#include<cmath>

bool notprime(char[], int);
char *baseconvt(char os[100], int from, int to);

int main() {
	FILE *stream;
	//freopen_s(&stream, "C:\\new\\C-small-attempt0.in", "r", stdin);
	freopen_s(&stream, "C:\\new\\ClargeLL.txt", "w", stdout);
	const int N = 32;
	const int J = 500;
	printf("Case #1:");
	char inputs[50];
	inputs[0] = '1';
	inputs[N - 1] = '1';
	inputs[N] = '\0';
	for (int i = 1;i < N - 1;i++) inputs[i] = '0';
	int output[9];
	memset(output, 0, sizeof(output));
	int sum = 0;
	while (sum < J) {
		int out[9];
		int test = 0;
		memset(out, 0, sizeof(out));
		char *s;
		for (int i = 2;i < 11;i++) {
			bool b = true;
			s = baseconvt(inputs, i, 10);
			for (int j = 2;j < 998;j++)
				if (notprime(s, j)) {
					out[i - 2] = j;
					test++;
					b = false;
					break;
				}
			if (b) break;
		}
		if (test == 9) {
			sum++;
			printf("\n%s", inputs);
			for (int i = 0;i < 9;i++)
				printf(" %d", out[i]);
		}
		inputs[N - 2]++;
		for (int dudu = N - 2;dudu > 0;dudu--) {
			if (inputs[dudu] > '1') {
				inputs[dudu] -= 2;
				inputs[dudu - 1]++;
			}
			else break;
		}
	}
	return 0;
}

bool notprime(char dividend[], int divisor) {
	static char quotient[100];
	int temp = 0;
	int i = 0, j = 0;
	while (dividend[i]) {
		temp = temp * 10 + (dividend[i] - 48);
		if (temp<divisor) {
			quotient[j++] = 48;
		}
		else {
			quotient[j++] = (temp / divisor) + 48;;
			temp = temp % divisor;
		}
		i++;
	}
	return (temp == 0);
}

char *baseconvt(char s[100], int from, int to)
{
	int fromL = strlen(s);
	int fs[100];
	memset(fs, 0, sizeof(fs));
	int k = 0;
	for (int i = fromL - 1; i >= 0; i--)
		fs[k++] = (int)(s[i] - 48);
	int toL = fromL * (from / to + 1);
	int ts[100];
	int cums[100];
	memset(ts, 0, sizeof(ts));
	memset(cums, 0, sizeof(cums));
	ts[0] = 1;
	for (int i = 0; i < fromL; i++)
	{
		for (int j = 0; j < toL; j++)
		{
			cums[j] += ts[j] * fs[i];
			int temp = cums[j];
			int rem = 0;
			int ip = j;
			do {
				rem = temp / to;
				cums[ip] = temp - rem*to; ip++;
				cums[ip] += rem;
				temp = cums[ip];
			} while (temp >= to);
		}
		for (int j = 0; j < toL; j++)
			ts[j] = ts[j] * from;
		for (int j = 0;j<toL;j++)
		{
			int temp = ts[j];
			int rem = 0;
			int ip = j;
			do
			{
				rem = temp / to;
				ts[ip] = temp - rem * to; ip++;
				ts[ip] += rem;
				temp = ts[ip];
			} while (temp >= to);
		}
	}
	char *outStr = new char[100];
	bool first = false;
	int strk = 0;
	for (int i = toL; i >= 0; i--)
	{
		if (cums[i] != 0) first = true;
		if (!first) continue;
		outStr[strk++] = cums[i] + 48;
	}
	outStr[strk] = '\0';
	return outStr;
}