#include <iostream>
#include <fstream>
using namespace std;
ofstream fout("result.txt");
int main()
{
	int n;
	cin >> n;
	getchar();
	for (int i = 1;i <= n;i++)
	{
		char s[2001], tmp[2001],min='1',max='1';
		int front = 1000,latter = 1000;
		int count = 0;
		cin >> tmp;
		do
		{
			if (tmp[count] >= 'A' && tmp[count] <= 'Z')
			{
				if (min == '1')
				{
					s[front] = tmp[count];
					min = tmp[count];
					max = tmp[count];
					front--;
					latter++;
				}
				else if (tmp[count] >= max)
				{
					s[front] = tmp[count];
					front--;
					max = tmp[count];
				}
				else
				{
					s[latter] = tmp[count];
					latter++;
					min = tmp[count];
				}
			}
			else
			{
				break;
			}
			count++;
		} while (count<strlen(tmp));
		fout << "Case #" << i << ": ";
		for (int j = front + 1;j < latter;j++)
		{
			fout << s[j];
		}
		fout << endl;
	}

	system("pause");
}