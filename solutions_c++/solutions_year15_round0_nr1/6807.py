#include<iostream>
#include<string>

using namespace std;
int main()
{
	/*freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);*/
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{

		int smax; cin >> smax;
		string s;
		cin >> s;
		int have = 0;
		have += ((int)s[0] - 48);
		int total = 0;
		for (int i = 1; i < s.size(); i++)
		{
			if (s[i] == '0') continue;
			if (i>have){
				total += (i - have);
				have += (i - have);

			}

			have += ((int)s[i] - 48);

		}
		cout << "Case #"<<i+1<<": "<< total << endl;
	}

}