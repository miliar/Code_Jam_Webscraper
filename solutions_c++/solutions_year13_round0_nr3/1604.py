#include <cstdio>
#include <cstring>
#include <algorithm>

int no;

long knowns[] = {1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001,10011001,10100101,10111101,11000011,11011011,11100111,11111111,20000002 }; 

void testCase(int no) 
{
	long A, B;
	scanf("%ld %ld", &A, &B);
	int iA, iB;
	iA = iB = 0;
	int i;
	for(i = 0; i < sizeof(knowns); i++)
	{
		long n = knowns[i];
		if(n * n >= A) {
			iA = i - 1;
			break;
		}
	} 

    for(; i < sizeof(knowns); i++)
    {
        long n = knowns[i];
        if(n * n > B) {
            iB = i - 1;
            break;
        }
    }
	printf("%d\n", iB - iA);
}

bool isPalindrome(long number, int bits) 
{
	if(number < 10) return true;

	char s[bits];
	sprintf(s, "%ld", number);
	if(s[bits - 1] == 0 || s[bits - 1] == '0') bits--;
	int l = 0, h = bits - 1;
//	printf("n=%ld,s=%s,bits=%d\n", number, s, bits);
	while(h > l)
	{
			
//		printf("l=%d,h=%d\n", s[l], s[h]);
		if(s[l++] != s[h--]) {
//			printf("not!\n");
			return false;
		}
	}
	return true;
}



int main()
{
	int N; scanf("%d", &N);
	
	for(no = 0; no < N; no++)
	{
		printf("Case #%d: ", no + 1);
		testCase(no);
	}
	return 0;	
}
