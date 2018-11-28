/******************************************************************************
 * Directives
 *****************************************************************************/
#ifdef WIN32
#define _CRT_SECURE_NO_WARNINGS
#endif

/******************************************************************************
 * Header Files
 *****************************************************************************/
#include <stdio.h>
#include <string.h>
#include <math.h>

/******************************************************************************
 * Constants, Macros, Typedefs, Enums & Structures
 *****************************************************************************/

/******************************************************************************
 * Global & Static Variables
 *****************************************************************************/
FILE *dbgout = stderr;

char g_inA[108];
char g_inB[108];

char g_A[108];
char g_B[108];
char g_C[108];
int g_lenA;
int g_lenB;
char g_rootC[56];

/******************************************************************************
 * Global & Static Function Prototypes
 *****************************************************************************/
void runCase();

/******************************************************************************
 * Function Implementations
 *****************************************************************************/
int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <=T; t++) {
		printf("Case #%d:", t);
		runCase();
	}

	return 0;
}

// -1 if a < b, 1 if a > b, 0 if a == b
inline int bufCompare(char *a, char *b, int alen, int blen)
{
	if (alen < blen) {
		return -1;
	} else if (alen > blen) {
		return 1;
	}
	for (int i = alen -1; i >= 0; i--) {
		char c = a[i] - b[i];
		if (c < 0) {
			return -1;
		} else if (c > 0) {
			return 1;
		}
	}
	return 0;
}

inline int intToBuf(char *buf, int x)
{
	int len = 0;
	while (x > 0) {
		int div = x / 10;
		int res = x - div * 10; // x % 10;
		buf[len] = (char)res;
		x = div;
		len++;
	}
	return len;
}

inline int llongToBuf(char *buf, long long x)
{
	int len = 0;
	while (x > 0) {
		long long div = x / 10;
		long long res = x - div * 10; // x % 10;
		buf[len] = (char)res;
		x = div;
		len++;
	}
	return len;
}

inline int bufToInt(char *buf, int len)
{
	int val = 0;
	for (int i = len - 1; i >= 0; i--) {
		val = val * 10;
		val += buf[i];
	}
	return val;
}

inline long long bufToLlong(char *buf, int len)
{
	long long val = 0;
	for (int i = len - 1; i >= 0; i--) {
		val = val * 10;
		val += buf[i];
	}
	return val;
}

inline void getSmallestPalindrome(char *buf, int len)
{
	int len_1 = len - 1;
	buf[0] = 1;
	for (int i = 1; i < len_1; i++) {
		buf[i] = 0;
	}
	buf[len_1] = 1;
}

void getNextPalindrome(char *buf, int *blen)
{
	int len = *blen;
	int half = len / 2;
	bool overflow = true;
	for (int i = half; i < len; i++) {
		if (buf[i] < 9) {
			buf[i]++;
			overflow = false;
			break;
		} else {
			buf[i] = 0;
		}
	}
	if (!overflow) {
		int len_1 = len - 1;
		for (int i = 0; i < half; i++) {
			buf[i] = buf[len_1 - i];
		}
	} else {
		len++;
		getSmallestPalindrome(buf, len);
		*blen = len;
	}
}

void getNextPalindrome2(char *buf, int *blen)
{
	int len = *blen;
	int half = len / 2;
	bool overflow = true;
	for (int i = half; i < len; i++) {
		if (buf[i] < 2) {
			buf[i]++;
			overflow = false;
			break;
		} else {
			buf[i] = 0;
		}
	}
	if (!overflow) {
		int len_1 = len - 1;
		for (int i = 0; i < half; i++) {
			buf[i] = buf[len_1 - i];
		}
	} else {
		len++;
		getSmallestPalindrome(buf, len);
		*blen = len;
	}
}

inline bool isPalindrome(char *buf, int len)
{
	int half = len / 2;
	int len_1 = len - 1;
	for (int i = 0; i < half; i++) {
		if (buf[i] != buf[len_1 - i]) {
			return false;
		}
	}
	return true;
}

bool bufSquare(char *dst, char *src, int slen)
{
	memset(dst, 0, slen * 2 - 1);

	for (int i = 0; i < slen; i++) {
		int sval = src[i];
		char *ddst;
		switch (sval) {
		case 1:
			ddst = &dst[i];
			for (int j = 0; j < slen; j++) {
				char res = ddst[j] + src[j];
				if (res > 9) {
					return false;
				}
				ddst[j] = res;
			}
			break;
		case 2:
			ddst = &dst[i];
			for (int j = 0; j < slen; j++) {
				char res = ddst[j] + (src[j] << 1);
				if (res > 9) {
					return false;
				}
				ddst[j] = res;
			}
			break;
		}
	}
	return true;
}

void dbgPrint(char *root, char *sq, int lenRoot, int lenSq)
{
	for (int i = 0; i < lenRoot; i++) {
		fprintf(dbgout, "%c", root[i] + '0');
	}
	fprintf(dbgout, "-");
	for (int i = 0; i < lenSq; i++) {
		fprintf(dbgout, "%c", sq[i] + '0');
	}
	fprintf(dbgout, "\n");
}

void runCaseBig()
{
	for (int i = 0; i < g_lenA; i++) {
		g_A[i] = g_inA[g_lenA - i - 1] - '0';
	}
	for (int i = 0; i < g_lenB; i++) {
		g_B[i] = g_inB[g_lenB - i - 1] - '0';
	}

	if (bufCompare(g_A, g_B, g_lenA, g_lenB) > 0) {
		printf(" 0\n");
		return;
	}

	int rootLen = g_lenA / 2 + 1;
	getSmallestPalindrome(g_rootC, rootLen);
	bool success = bufSquare(g_C, g_rootC, rootLen); // always success since it is smallest
	int compFront = bufCompare(g_C, g_A, rootLen * 2 - 1, g_lenA);
	while (compFront < 0) {
		getNextPalindrome2(g_rootC, &rootLen);
		success = bufSquare(g_C, g_rootC, rootLen);
		compFront = success ? bufCompare(g_C, g_A, rootLen * 2 - 1, g_lenA) : -1;
	}
	// here, success is true
	int compBack = bufCompare(g_C, g_B, rootLen * 2 - 1, g_lenB);
	long long cnt = 0;
	while (compBack <= 0) {
		if (success && isPalindrome(g_C, rootLen * 2 - 1)) {
			//dbgPrint(g_rootC, g_C, rootLen, rootLen * 2 - 1);
			cnt++;
		}
		getNextPalindrome2(g_rootC, &rootLen);
		success = bufSquare(g_C, g_rootC, rootLen);
		compBack = success ? bufCompare(g_C, g_B, rootLen * 2 - 1, g_lenB) : -1;
	}
	if (g_lenA == 1 && (g_lenB > 1 || g_B[0] == 9)) {
		cnt++;
	}
	printf(" %lld\n", cnt);
}

long long getRootGe(long long x)
{
	double dx = (double)x;
	double dy = sqrt(dx);
	long long y = (long long)dy;
	long long sq = y * y;
	if (sq == x) {
		return y;
	} else if (sq > x) {
		while (sq > x) {
			y--;
			sq = y * y;
		}
		if (sq == x) {
			return y;
		}
		// now y^2 < x < (y+1)^2
		return y + 1;
	} else {
		while (sq < x) {
			y++;
			sq = y * y;
		}
		// now x <= y^2
		return y;
	}
}

int getPalGe(int x, char *buf, int *blen)
{
	int len = intToBuf(buf, x);
	int half = len / 2;
	for (int i = 0; i < half; i++) {
		buf[i] = buf[len - 1 - i];
	}
	int pal = bufToInt(buf, len);
	if (pal < x) {
		getNextPalindrome(buf, &len);
		pal = bufToInt(buf, len);
	}
	*blen = len;
	return pal;
}

inline bool isPalindrome(long long x)
{
	char palBuf[20];

	int len = llongToBuf(palBuf, x);

	return isPalindrome(palBuf, len);
}

void runCaseSmall()
{
	long long a, b;
	sscanf(g_inA, "%lld", &a);
	sscanf(g_inB, "%lld", &b);
	if (a > b) {
		printf(" 0\n");
		return;
	}

	int rootA = (int)getRootGe(a);
	char palBuf[20];
	int len;
	int rootStart = getPalGe(rootA, palBuf, &len);

	int cnt = 0;
	int rootX = rootStart;
	long long x = (long long)rootX * rootX;
	while (x <= b) {
		if (isPalindrome(x)) {
			//fprintf(dbgout, "%d-%lld\n", rootX, x);
			cnt++;
		}
		getNextPalindrome(palBuf, &len);
		rootX = bufToInt(palBuf, len);
		x = (long long)rootX * rootX;
	}
	printf(" %d\n", cnt);
}

void runCase()
{
	scanf("%s %s", g_inA, g_inB);
	g_lenA = strlen(g_inA);
	g_lenB = strlen(g_inB);
	if (g_lenA > g_lenB) {
		printf(" 0\n");
		return;
	}
	if (g_lenB > 18) {
		runCaseBig();
	} else {
		runCaseSmall();
	}
}
