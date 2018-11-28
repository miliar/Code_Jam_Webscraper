#include<iostream>
#include<cstring>
//#pragma warning(disable:4996)
using namespace std;
int main()
{
	
	char input[101];
	//freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int t,i;
	int count = 1,len,match;
	cin >> t;
	char prev;
	while (t--)
	{
		cin >> input;
		len = strlen(input);
		prev = input[0];
		match = 0;
		for (i=0; i < len; i++)
		{
			if (prev != input[i])
			{
				match++;
			}
			prev = input[i];
		}
		if (input[len - 1] == '-')
		{
			match++;
		}
		cout << "Case #" << count << ": " << match << endl;
		count++;
	}

}
