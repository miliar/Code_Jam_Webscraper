#include "iostream"

using namespace std;

int track()
{
	int first, second;
	int arr[16];
	int ftest[4];
	int stest[4];

	cin >> first;
	first--;
	for (int i = 0; i < 16; i++)
	{
		cin >> arr[i];
	}
	for (int i = 0; i < 4; i++)
	{
		ftest[i] = arr[first * 4 + i];
	}
	cin >> second;
	second--;
	for (int i = 0; i < 16; i++)
	{
		cin >> arr[i];
	}
	for (int i = 0; i < 4; i++)
	{
		stest[i] = arr[second * 4 + i];
	}

	int flag = 0;
	int result = 0;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (ftest[i] == stest[j])
			{
				result = ftest[i];
				flag++;
			}
		}
	}
	if (flag == 0)
		return 0;
	else if (flag > 1)
		return -1;
	else 
		return result;
}

int main()
{
	int T;
	cin >> T;
	int result = 0;
	for (int i = 1; i <= T; i++)
	{
		result = track();
		if (result < 0)
			cout << "Case #" << i << ": Bad magician!" << endl;
		else if (result == 0)
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		else
			cout << "Case #" << i << ": " << result << endl;
	}
	
	//system("pause");
	return 0;
}