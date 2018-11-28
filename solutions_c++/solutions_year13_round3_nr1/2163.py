#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("file.in");
ofstream fout("file.out");

char str[1000000];
int len;
int result;
int n;

inline bool isConsonant(char ch)
{
	return (ch != 'a' && ch!= 'e' && ch!='i' && ch!= 'o' && ch != 'u');
}

void Go (int start)
{
	while (1)
	{
		int consecutive = 0;
		int i;
		for (i = start; i < len; i++)
		{
			if (isConsonant(str[i]))
			{
				consecutive++;
			} else {
				
				consecutive = 0;
			}
			if (consecutive >= n)
					break;
		}
		
		if (i != len || consecutive >= n)
		{
			int my = (i - n + 2 - start)*(len-i);
			result += my;
			start = i - n + 2;
		} else {
			break;
		}
	}
}

int main()
{
	int t;
	

	int i,r, k, j;
	int consecutive;
	int maxConsecutive;
	
	fin >> t;
	bool good;

	for (i =0 ; i < t; i++)
	{
		fin >> str >> n;

		result = 0;
		len = strlen(str);

		Go(0);

		fout << "Case #" << (i+1) << ": " << result << endl;
		/*for (r = 0; r < len; r++)
			flag[r] = 0;
		
		consecutive = 0;
		for (r = 0; r < len; r++)
		{
			if (r+n <= len)
			{
				good = true;
				for (int k = r; k < r+n; k++)
				{
					if (!isConsonant(str[k])
					{
						good = false;
						break;
					}
				}
				if (good)
		}	*/
	}
}