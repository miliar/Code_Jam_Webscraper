#include <bits/stdc++.h>

using namespace std;

bool digit[10] = {0};

bool check(int num)
{
	int i;
	for (; num; num /= 10)
		digit[num % 10] = true;
	for (i = 0; i < 10; i++)
	{
		if (!digit[i])
			return false;
	}
	return true;
}
int main()
{
	int b;
	scanf("%d", &b);

	int i = 0;
	int j;
	int k;
	do {
		i++;
		for (k = 0; k < 10; k++)
			digit[k] = false;
		cout << "Case #" << i << ": ";
		scanf("%d", &j);
		if (!j) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		k = j;
		for (k = j; !check(j); j += k);
		cout << j << endl;
	} while (i < b);
}