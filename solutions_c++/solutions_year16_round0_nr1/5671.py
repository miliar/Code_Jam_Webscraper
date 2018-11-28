#include <stdio.h>
#include <string.h>

int digits[1000];
int digitsLength;

void initDigits(long int number)
{
	int digit;
	int count = 0;
	while (number != 0) {
		digit = number % 10;
		digits[count] = digit;
		number /= 10;
		count++;
	}
	digitsLength = count;
}

long int countSheep (long int n)
{
	if (n == 0) {
		return -1;
	}

	int numberOfTries = 0,numberOfInsertion =0,i;
	int count[10];
	long int result =0;

	memset(digits,0,sizeof(digits));
	memset(count,0,sizeof(count));

	while (numberOfInsertion != 10) {
		result += n;
		initDigits(result);
		for (i = 0; i < digitsLength; i++) {
			if (count[digits[i]] == 0) {
				count[digits[i]] = 1;
				numberOfInsertion++;
			}
		}
		numberOfTries++;
	}

	return result;
}

void solve()
{
	freopen("A-large.in","r",stdin);
	freopen("sheep.out","w",stdout);

	long int N,resultReturned;
    int i, T;

    scanf("%d",&T);
    for (i = 1; i <= T; i++) {
	   scanf("%ld",&N);
	   printf("Case #%d: ",i);
	   resultReturned = countSheep(N);
	   if (resultReturned == -1) {
		   printf("INSOMNIA\n");
	   }else {
		   printf("%ld\n",resultReturned);
	   }
	}
}

int main()
{
    solve();
    return 0;
}