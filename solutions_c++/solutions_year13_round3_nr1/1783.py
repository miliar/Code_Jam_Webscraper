#include <iostream>
#include <math.h>
#include <string>

using namespace std;

bool isVowel(char c)
{
	if (c == 'a' || c=='o' || c=='i' || c=='u' || c=='e')
	{
		return true;
	}
	return false;
}

bool hasCons(string& str, int n)
{
	int count = 0;
	for(int i=0;i<str.length();i++)
	{
		if(!isVowel(str.at(i)))
			count++;
		else
			count = 0;
		if (count >= n)
		{
			return true;
		}
	}
	return false;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T = 0;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		string str;
		long res = 0;
		int n;
		cin >> str;
		cin >> n;

		for(int i=0;i<str.length();i++)
		{
			for(int j=i;j<str.length();j++)
			{
				if (j+1-i >= n)
				{
					if(hasCons(str.substr(i,j+1-i), n))
					{
						res++;
					}
				}
			}

		}

		cout << "Case #" << t+1 << ": " << res << endl;

		/*while (true)
		{
			for(int i=0;i<str.length();i++)
			{

			}
		}*/
	}
}