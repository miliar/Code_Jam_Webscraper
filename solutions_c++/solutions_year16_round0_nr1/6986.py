#include <cstdio>

#define TEST_PRINT_INPUT 0
#define TEST_PRINT_INCREMENT_CHECK 0
#define TEST_PRINT_POWER10 0
#define TEST_PRINT_NUM 0
#define TEST_PRINT_N_MULTIPLE 0
#define TEST_ONCE 0

#define MAX_POWER10 19
#define MAX_CHECK 10

unsigned long long power10[MAX_POWER10] {
	10ULL,
	100ULL,
	1000ULL,
	10000ULL,
	100000ULL,
	1000000ULL,
	10000000ULL,
	100000000ULL,
	1000000000ULL,
	10000000000ULL,
	100000000000ULL,
	1000000000000ULL,
	10000000000000ULL,
	100000000000000ULL,
	1000000000000000ULL,
	10000000000000000ULL,
	100000000000000000ULL,
	1000000000000000000ULL,
	10000000000000000000ULL};

struct Check {
	static char increment;
	char chr;
	bool set;
	Check() {
		chr = increment;
		set = false;
		increment++;
	};
	static bool isDone(Check *ptr, const int &size) {
		for (int i=0; i < size; i++) {
			if (!(ptr + i)->set)return false;	
		}
		return true;
	};
};

char Check::increment = '0';

void getDigits(const unsigned long long &value, Check * check) {
	for (int i = 0; i < MAX_POWER10 + 1; i++) {
		int num;
		if (i == 0) {
			num = value % power10[i];
		} else if (i == MAX_POWER10) {
			num = value / power10[i - 1];
		} else {
			if ((unsigned long long)(value / power10[i - 1]) == 0)break;
			unsigned long long tmp = value % power10[i];
			num = tmp / power10[i - 1];
		}
		(check + num)->set = true;
#if TEST_PRINT_NUM
		printf("%d ", num);
#endif
	}
#if TEST_PRINT_NUM
	printf("\n");
#endif
}; 

int main() {
	int t;
	Check *listCheck = new Check[MAX_CHECK];
	unsigned long long n;
	int ret = scanf("%d", &t);
#if TEST_PRINT_INPUT 
	printf("T = %d\n", t);
#endif
#if TEST_PRINT_INCREMENT_CHECK
	for (int i = 0; i < 10; i++) {
		printf("%c ", listCheck[i].chr);
	}
#endif
#if TEST_PRINT_POWER10
	for (int i= 0; i < MAX_POWER10 + 1; i++) {
		printf("%llu\n", power10[i]);
	}
#endif
	for (int i=0; i < t; i++) {
		if (listCheck == 0) {
			Check::increment = '0';
			listCheck = new Check[MAX_CHECK];
		}
		ret = scanf("%llu", &n);
		unsigned long long nold, nicre, increment = 2;
		bool insomia = false;
#if TEST_PRINT_INPUT 
		printf("N = %llu\n", n);
#endif
		nicre = n;
		getDigits(n, listCheck);
		while(!Check::isDone(listCheck, MAX_CHECK)) {
			nold = nicre;
			nicre  = (unsigned long long)(n + nicre);
#if TEST_PRINT_N_MULTIPLE 
			printf("%dN =", increment);
			printf(" %llu\n", nicre);
#endif
			if (nicre == nold){ 
				insomia = true;
				break;
			}
			increment++;
			getDigits(nicre, listCheck);
		} 
		if (!insomia)
			printf("Case #%d: %llu\n", (i + 1), nicre);
		else printf("Case #%d: INSOMNIA\n", (i + 1));
#if TEST_ONCE 
		break;
#endif
		delete[] listCheck;
		listCheck = 0;
	}
	return 1;
};