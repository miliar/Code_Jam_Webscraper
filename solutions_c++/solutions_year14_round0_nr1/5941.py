#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int tc;
	cin >> tc;
	for(int cn = 1; cn <= tc; cn++)
	{
		int firstAns;
		cin >> firstAns;

		vector<int> c1;
		vector<int> c2;
		for(int i = 0; i < 16; i++)
		{
			int x;
			cin >> x;
			c1.push_back(x);
		}

		int secAns;
		cin >> secAns;
		for(int i = 0; i < 16; i++)
		{
			int x;
			cin >> x;
			c2.push_back(x);
		}

		vector<int> posAnswer;
		firstAns -= 1;
		secAns -= 1;
		int i = firstAns*4;
		for(int j = 0; j < 4; j++)
		{
			int x = c1[i];
			posAnswer.push_back(x);
			i++;
		}

		vector<int> posAns2;
		i = secAns*4;
		for(int j = 0; j < 4; j++)
		{
			int x = c2[i];
			posAns2.push_back(x);
			i++;
		}

		vector<int> ans;
		//check for any same answers
		for(i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(posAnswer[i] == posAns2[j])
				{
					ans.push_back(posAnswer[i]);
				}
			}
		}
		cout << "Case #" << cn << ": ";
		if(ans.size() == 0)
		{
			cout << "Volunteer cheated!";
		}
		else if(ans.size() == 1)
		{
			cout << ans[0];
		}
		else
		{
			cout << "Bad magician!";
		}
		cout << endl;
	}
	return 0;
}

