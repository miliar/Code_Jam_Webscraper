#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main(void)
{
	ifstream input("B-large.in");
	ofstream output("outputLarge.out");
	string len;
	getline(input,len);
	int numCases = atoi(len.c_str());
	int m,n;
	string s1,s2;
	for (int i = 0; i < numCases; i++)
	{
		int cnt = 0;
		getline(input,s1);
		n = atoi(s1.substr(0,s1.find(' ')).c_str());
		m = atoi(s1.substr(s1.find(' ')+1).c_str());
		vector<int> arr(n*m,0);
		vector<bool> arrChecked(n*m,false);
		for ( int j = 0 ; j < n ; j++ )
		{
			getline(input,s2);
			int lastSpace = 0;
			for (int k = 0; k < m ; k++)
			{
				arr[j*m+k] = atoi(s2.substr(0,s2.find(' ')).c_str());
				s2 = s2.substr(s2.find(' ')+1);
			}
			for (int k = 0; k < m ; k ++)
			{
				if (arrChecked[j*m+k])
					continue;
				bool canBeDone = true;
				vector<int> index;
				for (int l = 0; l < m ; l++)
				{
					if (arr[j*m+l]==arr[j*m+k])
						index.push_back(j*m+k);
					else if (arr[j*m+l] > arr[j*m+k])
					{
						canBeDone = false;
						break;
					}
				}
				if (canBeDone)
				{
					for ( int o = 0; o < index.size() ; o++ )
						{
							arrChecked[index[o]] = true;
							cnt++;
						}
				}
			}
		}
		for (int k = 0 ; k < m ; k++)
		{
			for (int l = 0; l < n ; l++)
			{
				if (!arrChecked[l*m+k])
				{
					bool canBeDone = true;
					vector<int> index;
					for (int o = 0; o < n ; o++)
					{
						if (arr[l*m+k]==arr[o*m+k])
							index.push_back(l*m+k);
						else if (arr[o*m+k] > arr[l*m+k])
						{
							canBeDone = false;
							break;
						}
					}
					if (canBeDone)
					{
						for ( int o = 0 ; o < index.size() ; o++ )
						{
							arrChecked[index[o]] = true;
							cnt++;
						}
					}
				}

			}
		}
		output << "Case #" << i+1 << ": ";
		bool yesOrNo = true;
		for (int o = 0 ; o < arrChecked.size() ; o++)
		{
			if (arrChecked[o] == false)
				yesOrNo = false;
		}
		if (yesOrNo)
			output << "YES";
		else 
			output << "NO";
		output << endl;
	}
	input.close();
	output.close();
	return 0;
}
