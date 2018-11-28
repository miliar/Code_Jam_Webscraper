#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int numTest, cntTest = 0;
	//char name[1000000];
	string name;
	char tmp[100000];
	unsigned int n;

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	cin >> numTest;
	while (++cntTest <= numTest)
	{
		cin >> name >> n;
		//int len = strlen(name);
		int len = name.length();
		int score = 0;

		for (int i = 0; i <= len - n; i++)
		{
			for (int j = i + n; j <= len; j++)
			{
				char* p;
				string sub = name.substr(i, j - i);
				strcpy(tmp, sub.c_str());
				p = strtok(tmp, "aeiouAEIOU");

				while (p != NULL) {
					if (strlen(p) >= n)
					{
						score++;
						break;
					}
					p = strtok(NULL, "aeiouAEIOU");
				}
			}
		}
		//for (int i = 0; i <= len - n; i++)
		//{
		//	int j;
		//	for (j = 0; j < n; j++)
		//		if (name[i + j] == 'a' || name[i + j] == 'e' || name[i + j] == 'i' || 
		//			name[i + j] == 'o' || name[i + j] == 'u')
		//			break;
		//	if (j == n)
		//		score += len - j + 1;
		//}
		cout << "Case #" << cntTest << ": " << score << endl;
	}
	return 0;
}
