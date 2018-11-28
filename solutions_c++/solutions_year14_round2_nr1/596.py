#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int Tn;
int n;
string s[110];
int pos[110];

int getlen(string ss, char ch)
{
	int res = 0;
	for (int i=0;i<ss.length() && ss[i]==ch;i++) 
		res++;
	return res;
}

bool checkpos()
{
	for (int i=0;i<n;i++)
		if (pos[i]<s[i].length())
			return true;
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int i;

	cin >> Tn;
	for (int T=1;T<=Tn;T++)
	{
		cin >> n;
		cin.ignore();
		for (i=0;i<n;i++)
			getline(cin, s[i]);

		int ans = 0;
		bool flag = true;
		memset(pos, 0, sizeof pos);

		while (checkpos())
		{
			char ch = s[0][pos[0]];
			vector<int> len;
			for (i=0;i<n;i++)
			{
				int tmp = getlen(s[i].substr(pos[i]), ch);
				if (!tmp)
				{
					flag = false;
					break;
				}
				else
				{
					len.push_back(tmp);
					pos[i] += tmp;
				}
			}
			if (!flag)
				break;
			sort(len.begin(),len.end());
			int tmp = len[len.size()/2];
			for (i=0;i<n;i++)
				ans += abs(len[i]-tmp);
		}


		cout << "Case #" << T << ": ";
		if (!flag)
			cout << "Fegla Won" << endl;
		else
			cout << ans << endl;
	}
}