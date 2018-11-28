#include <iostream>
#include <cstdio>
#include <string>
#include <vector> 

using namespace std;
vector <int> word(100);
vector <int> how(30);

string target, keyboard;
int k, l , s;
int max_number;
int all;
int ans;

int count()
{
	int res = 0;
	// cout << target << "\n";
	for (int left = 0; left < s; ++left)
	{
		//cout << word[left];
		int right = left + target.size() - 1;
		if (right >= s)
			continue;
		bool flag = true;
		for (int i = left; i <= right; ++i)
		{
			if (word[i] != int(target[i - left] - 'A'))
			{
				flag = false;
				continue;
			}
		}
		res += int(flag);
	}
	//cout << "\n";
	return res;
}

void gen(int n)
{
	// cout << n << " " << s << "\n";
	if (n == s)
	{
		max_number = max(count(), max_number);
		all++;
		ans += count();
		return;
	}

	for (int i = 0; i < 26; ++i)
	{
		for (int j = 0; j < how[i]; ++j)
		{
			word[n] = i;
			gen(n + 1);
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TEST;
	cin >> TEST;
	for (int test = 1; test <= TEST; ++test)
	{
		cin >> k >> l >> s;
		max_number = 0;
		all = 0;
		ans = 0;
		cin >> keyboard;
		cin >> target;
		for (int i = 0; i < 26; ++i)
		{
			how[i] = 0;
		}
		//cout << keyboard << endl;
		for (int i = 0; i < keyboard.size(); ++i)
		{
			// cout << int(keyboard[i] - 'A') << " ";
			how[int(keyboard[i] - 'A')]++;
		}
		/*for (int i = 0 ; i < 26; ++i)
		{
			cout << how[i] << " ";
		}*/
		//cout << "\n";	
		gen(0);
		//cout << max_number << " " << ans << " " << all << "\n";
		printf("Case #%d: %.9lf\n", test, 1.0 * max_number - (ans * 1.0) / (1.0 * all ));
	}
}
