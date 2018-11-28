#include <iostream>
#include <string.h>
using namespace std;

bool check(bool checklist[])
{
	for (int i = 0 ; i < 10; i++)
		if (checklist[i] == false)
			return false;
	return true;
}

void calc(bool checklist[], unsigned int x)
{
	while(x)
	{
		checklist[x%10] = true;
		x = x/10;

	}
}

int main()
{
	
		int cases, last;
		unsigned long int N, prev = 0, curr;
		int size;
		int multfac = 2;
		bool checklist[10];
		int cnt = 1;
		cin >> cases;
		for (int x = 1; x <= cases; x++)
		{
			cin >> N;
			
			for (int i = 0 ; i < 10; i++)
				checklist[i] = false;
			prev = 0;
			cnt = 1;			
			while (!check(checklist))
			{
				curr = N*cnt++;
				if (curr == prev)
					break;
				calc(checklist, curr);
				prev = curr;
			}
			
			if (check(checklist))
				cout << "Case #" << x << ": " << curr << endl;
			else
				cout << "Case #" << x << ": " << "INSOMNIA" << endl;
		}
		return 0;
}

