#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ifstream inData;
	ofstream outData;
	
	int T = 0;
	string S;
	int y;
	int tempLength;

	inData.open("B-large.in");
	outData.open("pancakes.txt");

	inData >> T;
	getline(inData,S);

	for (int x = 1; x <= T; x++)
	{
		S = "";
		y = 0;

		getline(inData,S);
		tempLength = S.length();

		for (int checker = tempLength; checker > 0; checker--)
		{
			if (S[checker - 1] == '-')
			{
				string problemArea = S.substr(0, checker);
				while (problemArea[checker - 1] == '-')
				{
					string holder = problemArea;
				
					if (problemArea[0] == '-')
					{
						for (int replacer = checker - 1; replacer >= 0; replacer--)
						{
							problemArea[replacer] = holder[checker - 1 - replacer];
							if (problemArea[replacer] == '-')
								problemArea.replace(replacer, 1, "+");
							else if (problemArea[replacer] == '+')
								problemArea.replace(replacer, 1, "-");
						}
						y++;
					}
					else
					{
						int minuses = 0;

						while ((problemArea[problemArea.length() - 1] == '-') && (problemArea.length() > 1))
						{
							problemArea = problemArea.substr(0, problemArea.length() - 1);
							minuses++;
						}

						holder = problemArea;

						int length = problemArea.length();

						for (int i = 0; i < length; i++)
						{
							problemArea[i] = holder[length - i - 1];
							if (problemArea[i] == '-')
								problemArea.replace(i, 1, "+");
							else if (problemArea[i] == '+')
								problemArea.replace(i, 1, "-");
						}

						y++;
						problemArea.append(minuses, '-');
					}
				}
				S.replace(0, checker, problemArea);
			}
		}
		outData << "Case #" << x << ": " << y << endl;
	}

	inData.close();
	outData.close();

	return 0;
}