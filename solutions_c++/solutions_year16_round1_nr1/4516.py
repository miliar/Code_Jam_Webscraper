#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

string word[200];

int main(void)
{
	freopen("inputAA.txt", "r", stdin);
	freopen("outputAA.txt", "w", stdout);

	int t;
	int n;

	char alp;
	char first;

	scanf("%d", &t);
	getchar();
	for (int i = 0; i < t; i++)
	{
		while (1)
		{
			scanf("%c", &alp);
			if (alp == '\n') break;
			if (word[i].empty() == 1)
			{
				word[i] = word[i] + alp;
				first = alp;
			}
			else if (first > alp)
			{
				word[i] = word[i] + alp;
			}
			else if (first <= alp)
			{
				word[i] = alp + word[i];
				first = alp;
			}
		}
		cout <<"Case #"<< i+1 << ": " << word[i] << endl;
	}
	
}