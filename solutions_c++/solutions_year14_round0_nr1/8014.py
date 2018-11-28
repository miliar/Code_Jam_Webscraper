#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int one, two;
		int tempa, tempb;
		int oneArr[4];
		int twoArr[4];
		cin >> one;
		for (int a = 1; a <= 4; a++)
		{
			for (int ai = 1; ai <= 4; ai++)
			{
				cin >> tempa;
				if (a == one)
				{
					oneArr[ai-1] = tempa;
				}
			}
		}
		cin >> two;
		for (int a = 1; a <= 4; a++)
		{
			for (int ai = 1; ai <= 4; ai++)
			{
				cin >> tempb;
				if (a == two)
				{
					twoArr[ai-1] = tempb;
				}
			}
		}
		vector<int> answer;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (oneArr[j] == twoArr[k])
				{
					answer.push_back(oneArr[j]);
				}
			}
		}
		cout << "Case #" << i << ": ";
		if (answer.size() == 0)
		{
			cout <<  "Volunteer cheated!" << endl;
		}
		else if (answer.size() > 1)
		{
			cout << "Bad magician!" << endl;
		} 
		else 
		{
			cout << answer[0] << endl;
		}
	}
	return 0;
}