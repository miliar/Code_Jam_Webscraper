#include "stdio.h"
#include "string.h"
#include "math.h"
#include "deque"

using namespace std;
#define debug(...) 
//#define debug(...) printf("[debug]");printf(__VA_ARGS__);

deque<unsigned long long> palindrome_list;

bool is_palindrome(unsigned long long n)
{
	static char str[128] = {'\0'};
	int i, len;
	memset(str, '\0', 128);

	sprintf(str, "%llu", n);
	len = strlen(str);
	for (i = 0 ; i < len/2; ++i)
		if (str[i] != str[len-i-1])
			return false;
	return true;
}

void pre_gen()
{
	unsigned long long n = 0;
	unsigned long long i = 1;
	//palindrome_list.resize(1<<5);
	for (i = 1 ; i <= 1e7; ++i)
	{
		n += i + i - 1;
		//debug("Testing %llu\n", n);
		if (is_palindrome(i) && is_palindrome(n))
			palindrome_list.push_back(n);
	}
	
#ifdef debug
	for (deque<unsigned long long>::iterator itr = palindrome_list.begin(); itr != palindrome_list.end(); ++itr)
	{
		debug("Palindrome: %llu\n", *itr);
	}
#endif
}

int main()
{
	int T, A, B;
	int c;

	pre_gen();
	scanf("%d\n", &T);
	
	for (c = 1; c <= T; ++c)
	{
		unsigned long long count = 0;
		scanf("%d %d\n", &A, &B);
		
		for (deque<unsigned long long>::iterator itr = palindrome_list.begin(); itr != palindrome_list.end(); ++itr)
		{
			if (*itr >= A && *itr <= B)
				count++;
			if (*itr > B)
				break;
		}

		printf("Case #%d: %lld\n", c, count);
	}
	return 0;
}
