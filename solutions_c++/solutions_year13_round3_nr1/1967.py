#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <string>

using namespace std;

bool isVowel(char c)
{
	if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
		return true;
	else
		return false;
}

int main(int argc, char* argv[])
{
	int T;
	cin >> T;

	for (int caseId = 1; caseId <= T; caseId++)
	{
		string name = "";
		int n;
		cin >> name >> n;

		int nameLen = name.length(); 
		if (n > nameLen)
		{
			cout << "Case #" << caseId << ": " << 0 << endl;
			continue;
		}

		int cnt = 0;
		int lPos = 0;
		int nValue = 0;
		for (int i = 0; i < nameLen; i++)
		{
			if (isVowel(name[i])) {
				cnt = 0;
				continue;
			}else{
				cnt++;
			}

			if (cnt == n)
			{
				nValue += (i-lPos+1-n+1)*(nameLen-i);
				lPos = i - (n-2);
			}else if (cnt > n)
			{
				nValue += nameLen-i;
				lPos++;
			}
																
		}

		cout << "Case #" << caseId << ": " << nValue << endl;
	}


	return 0;
}

