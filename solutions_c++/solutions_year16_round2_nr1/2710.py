#include <iostream>
#include <string>
#include <string.h>
using namespace std;

int ans[10];
int abc[26];
int main()
{
	int T, tm;
	string st;

	cin >> T;
	for (int k = 0; k < T;k++)
	{

		cin >> st;
		int n = st.size();
		memset(abc, 0, sizeof(abc));
		memset(ans, 0, sizeof(ans));
		for (int i = 0; i < n; i++)
		{
			abc[st[i] - 'A']++;
		}
		//0
		ans[0] = abc['Z' - 'A'];
		abc['Z' - 'A'] = 0;
		abc['E' - 'A'] -= ans[0];
		abc['R' - 'A'] -= ans[0];
		abc['O' - 'A'] -= ans[0];
		//2
		ans[2] = abc['W' - 'A'];
		abc['W' - 'A'] = 0;
		abc['T' - 'A'] -= ans[2];
		abc['O' - 'A'] -= ans[2];
		//4
		ans[4] = abc['U' - 'A'];
		abc['U' - 'A'] = 0;
		abc['O' - 'A'] -= ans[4];
		abc['F' - 'A'] -= ans[4];
		abc['R' - 'A'] -= ans[4];
		//1
		ans[1] = abc['O' - 'A'];
		abc['O' - 'A'] = 0;
		abc['N' - 'A'] -= ans[1];
		abc['E' - 'A'] -= ans[1];
		//3
		ans[3] = abc['R' - 'A'];
		abc['R' - 'A'] = 0;
		abc['T' - 'A'] -= ans[3];
		abc['H' - 'A'] -= ans[3];
		abc['E' - 'A'] -= 2*ans[3];

		//5
		ans[5] = abc['F' - 'A'];
		abc['F' - 'A'] = 0;
		abc['I' - 'A'] -= ans[5];
		abc['V' - 'A'] -= ans[5];
		abc['E' - 'A'] -= ans[5];
		//6
		ans[6] = abc['X' - 'A'];
		abc['X' - 'A'] = 0;
		abc['S' - 'A'] -= ans[6];
		abc['I' - 'A'] -= ans[6];
		//7
		ans[7] = abc['V' - 'A'];
		abc['V' - 'A'] = 0;
		abc['S' - 'A'] -= ans[7];
		abc['E' - 'A'] -= 2*ans[7];
		abc['N' - 'A'] -= ans[7];
		//8
		ans[8] = abc['G' - 'A'];
		abc['G' - 'A'] = 0;
		abc['E' - 'A'] -= ans[8];
		abc['I' - 'A'] -= ans[8];
		abc['H' - 'A'] -= ans[8];
		abc['T' - 'A'] -= ans[8];
		//9
		ans[9] = abc['E' - 'A'];

		cout << "Case #"<<k+1<<": ";
		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < ans[i]; j++)
			{
				cout<<i;
			}
		}
		cout << endl;
	}
	return 0;
}