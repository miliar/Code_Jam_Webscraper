#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int T, z = 1, i;
	scanf("%d", &T);
	getchar();
	while(T--)
	{
		int A[26] = {0};
		char c;
		for(i = 0; i< 26; i++)
			A[i] = 0;
		while((c = getchar()) != '\n')
		{
			A[(int)c - 'A']++;
		}

		int arr[10] = {0};
		for(i = 0; i< 10; i++)
			arr[i] = 0;
		arr[0] = A['Z' - 'A'];
		A['Z' - 'A'] -= arr[0];A['E' - 'A'] -= arr[0];A['R' - 'A'] -= arr[0];A['O' - 'A'] -= arr[0];
		arr[6] = A['X' - 'A'];
		A['S' - 'A'] -= arr[6];A['I' - 'A'] -= arr[6];A['X' - 'A'] -= arr[6];
		arr[8] = A['G' - 'A'];
		A['E' - 'A'] -= arr[8];A['I' - 'A'] -= arr[8];A['G' - 'A'] -= arr[8];A['H' - 'A'] -= arr[8];A['T' - 'A'] -= arr[8];
		arr[7] = A['S' - 'A'];
		A['S' - 'A'] -= arr[7];A['E' - 'A'] -= arr[7];A['V' - 'A'] -= arr[7];A['E' - 'A'] -= arr[7];A['N' - 'A'] -= arr[7];
		arr[3] = A['H' - 'A'];
		A['T' - 'A'] -= arr[3];A['H' - 'A'] -= arr[3];A['R' - 'A'] -= arr[3];A['E' - 'A'] -= arr[3];A['E' - 'A'] -= arr[3];
		arr[4] = A['R' - 'A'];
		A['F' - 'A'] -= arr[4];A['O' - 'A'] -= arr[4];A['U' - 'A'] -= arr[4];A['R' - 'A'] -= arr[4];
		arr[5] = A['F' - 'A'];
		A['F' - 'A'] -= arr[5];A['I' - 'A'] -= arr[5];A['V' - 'A'] -= arr[5];A['E' - 'A'] -= arr[5];
		arr[2] = A['W' - 'A'];
		A['T' - 'A'] -= arr[2];A['W' - 'A'] -= arr[2];A['O' - 'A'] -= arr[2];
		arr[1] = A['O' - 'A'];
		A['O' - 'A'] -= arr[1];A['N' - 'A'] -= arr[1];A['E' - 'A'] -= arr[1];
		arr[9] = A['I' - 'A'];

		printf("Case #%d: ",z);
		for(int j = 0; j < 10; ++j)
		{
			if(arr[j] != 0)
			{
				int count  = arr[j];
				while(count--)
					printf("%d",j);
			}
		}
		printf("\n");

		z++;
		
	}
	
	return 0;
}