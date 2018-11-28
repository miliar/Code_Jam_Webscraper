#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

bool isVowel(char c)
{
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool valid(string str, int N)
{
	int consc = 0;
	for(int i = 0; i<str.size(); i++)
	{
		if(!isVowel(str[i]))
			consc++;
		else
			consc = 0;
		if(consc == N)
			return true;
	}
	return false;
}

int main()
{

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int ans;
	string str;
	int T, N;
	cin >> T;

	for(int t=1; t<=T; t++)
	{

		ans = 0;
		cin >> str >> N;
		for(int i=0; i<(int)str.size(); i++)
		{
			for(int j=1; i+j<=(int)str.size(); j++)
			{
				if(valid(str.substr(i,j),N))
					ans ++;
			}
		}
		cout << "Case #" << t << ": ";
		cout << ans << endl;
	}

	return 0;
}
