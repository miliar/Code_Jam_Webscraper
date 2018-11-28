#include<iostream>
#include <string>
#include<vector>
using namespace std;
int main()
{
	int nTests = 0;
	cin >> nTests;
	int n = 0;
	for (int i = 1; i <= nTests; i++)
	{
		cin >> n;
		vector<char>chiffresGen;
		bool allGen = false;
		int n2;
		int j = 0;
		string chiffres;
		while (!allGen)
		{
			j++;
			n2 = j*n;
			chiffres = to_string(n2);
			int counter = 0;
			for (int k = 0; k < chiffres.length(); k++)
			{
				bool existe = false;
				for (int l = 0; l < chiffresGen.size(); l++)
				{
					if (chiffresGen[l] == chiffres[k])
					{
						existe = true;
						counter++;
						break;
					}
				}
				if (!existe)
				{
					chiffresGen.push_back(chiffres[k]);
				}
			}
			if (chiffresGen.size() == 10)
			{
				cout << "Case #" << i << ": " << n2 << endl;
				allGen = true;
			}
			else if ((counter == chiffresGen.size()) && (counter == chiffres.size()))
			{
				cout << "Case #" << i << ": " << "INSOMNIA" << endl;
				allGen = true;
			}
		}
	}
	//system("pause");
}