#include <iostream>
#pragma warning(disable: 4996)
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Tests;
	cin >> Tests;
	int Possibilities1[4];
	int Possibilities2[4];
	int Answers[4];
	for (int n = 0; n<Tests; n++)
	{
		int ans, k;
		cin >> ans;
		for (int i = 0; i<4; i++)
			for (int j = 0; j<4; j++)
			{
				if (i==ans-1)
					cin >> Possibilities1[j];
				else
					cin >> k;
			}
		cin >> ans;
		for (int i = 0; i<4; i++)
			for (int j = 0; j<4; j++)
			{
				if (i==ans-1)
					cin >> Possibilities2[j];
				else
					cin >> k;
			}
		int count = 0;
		for (int i = 0; i<4; i++)
			for (int j = 0; j<4; j++)
				if (Possibilities1[i]==Possibilities2[j])
				{
					Answers[count] = Possibilities1[i];
					count++;
				}
		cout <<	"Case #" << n+1 << ": ";
		if (count==1)
			cout << Answers[0];
		else
			if (count>1)
				cout << "Bad magician!";
			else
				if (count==0)
					cout << "Volunteer cheated!";
		cout << endl;
	}
	return 0;
}