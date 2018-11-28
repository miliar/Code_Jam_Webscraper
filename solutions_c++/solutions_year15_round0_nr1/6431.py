# include <iostream>
# include <string>

using namespace std;

int get_min(string s)
{
	int count = 0, required = 0, i;

	for(i = 0; i < s.size(); i++)
	{
		if (count >= i)
		{
			count += s[i] - '0';
			continue;
		}
		else
		{
			required += i - count;
			count += i - count + s[i] - '0';
		}
	}
	return required;

}

int main()
{
	int t, n, i = 1;
	string s;

	cin >> t;

	while(i <= t)
	{
		cin >> n >> s;
		cout << "Case #" << i << ": " << get_min(s) << endl;
		i = i+1;
	}
	return 0;
}