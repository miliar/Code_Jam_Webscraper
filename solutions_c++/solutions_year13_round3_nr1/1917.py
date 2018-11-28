#include<iostream>
#include<string>
#include<vector>

using namespace std;


bool voyelle(char c)
{
	return((c == 'a')||(c == 'e')||(c == 'i')||(c == 'o')||(c == 'u'));
}

int main()
{
	int cases = 0;
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		cases++;
		string mot;
		cin >> mot;
		int length = 0;
		int n;
		cin >> n;
		int consec = 0;
		int result = 0;
		int lastzero = 0;
		length = mot.size();
		int lastconsec = length;
		for(int j = length-1; j >= 0; j--)
		{
			if(consec > 0)
				result += consec;
			if(voyelle(mot[j]))
				lastzero = 0;
			else
			{
				if(lastzero == n-1)
				{
					if(lastconsec == j+1)
					{
						consec++;
						lastconsec = j;
						result++;
					}
					else
					{
						if(lastconsec != length)
						{
							consec += (lastconsec)-j;
							result += lastconsec-j;
							lastconsec = j;
						}
						else
						{
							consec += lastconsec-(j+n-1);
							result += lastconsec-(j+n-1);
							lastconsec = j;
						}
					}
				}
				else
					lastzero++;
			}
		}
		cout << "Case #" << cases << ": " << result << endl;
	}
}
