#include<algorithm>
#include<cstdio>
#include<set>
#include<iostream>
using namespace std;
int helperNumber = -1;
void readData(int number, std::set<int>& myset)
{
	//row ; column
	for (int l = 0; l < 4; l++)
	{
		if (l == number - 1)
		{
			for (int k = 0; k < 4; k++)
			{
				int f;
				scanf("%d", &f);
				if (myset.count(f))
					helperNumber = f;
				myset.insert(f);
			}
		}
		else
		{
			int f;
			for (int k = 0; k < 4; k++)
			{
				scanf("%d", &f);
			}

		}
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		std::set<int> myset;
		int first, second;
		scanf("%d", &first);
		readData(first, myset);
		scanf("%d", &second);
		readData(second, myset);
		int setSize = myset.size();
		if (setSize == 7)
		{
			cout << "Case #" << i + 1 << ": " << helperNumber << endl;
		}
		else if (setSize == 8) 
		{
			cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		}
		else if (setSize == 4 || setSize == 5 || setSize == 6)
		{
			cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
		}

	}
	return 0;
}