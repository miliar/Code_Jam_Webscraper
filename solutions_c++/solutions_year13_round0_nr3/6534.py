#include <cstdlib>
#include <cstdio>

bool palindrome (int n)
{
		int arr[5];
		int i = 0, len;

	while(n) {

		arr[i++] = n%10;
		n		 = n/10;
	}

	len = i - 1;

	for (i = 0; i <= len/2; i++) {

		if (arr[i] != arr[len - i])
			return false;
	}

	return true;
}

int main ()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out3s.txt", "w", stdout); 

	int	tc, i, a, b, count;
	int arr[1001] = {0};
	bool ispal;

	scanf("%d", &tc);

	for (i = 1; i <= 1000; i++) {

		if (arr[i] != 0)
			continue;

		ispal = palindrome(i);

		if (ispal == false) {

			arr[i] = 1;
			i*i <= 1000 ? arr[i*i] = 1 : 1;
		
		} else if (ispal == true && i*i <= 1000) {
			
			if (palindrome(i*i))
				arr[i*i] = 2;
			else
				arr[i*i] = 1;
		}
	}

	for (i = 1; i <= tc; i++)	{

		count= 0;
		scanf("%d%d", &a, &b);

		for (int j = a; j <=b; j++) {

			if (arr[j] == 2)
				count++;
		}

		printf("Case #%d: %d\n", i, count);

	}

	return 0;
}