#include <bits/stdc++.h>
using namespace std;
// define 1 -> 1 , 2 -> i, 3 -> j, 4 -> k
int main()
{
	map<char,int> m;
	m['1'] = 1, m['i'] = 2, m['j'] = 3, m['k'] = 4;
	int ch[5][5];
	ch[1][1] = 1;
	ch[2][2] = ch[3][3] = ch[4][4] = -1;
	ch[4][3] = -2;
	ch[2][1] = ch[1][2] = ch[3][4] = 2;
	ch[2][4] = -3;
	ch[3][1] = ch[1][3] = ch[4][2] = 3;
	ch[3][2] = -4;
	ch[4][1] = ch[1][4] = ch[2][3] = 4;

	int t, n, k;
	cin >> t;
	for(int p = 1; p <= t; p++)
	{
		cin >> n >> k;
		string tmp, str = "";
		cin >> tmp;
		while(k--)
			str += tmp;
		int ans[10240] = {}, len = str.size();
		bool b[10240];
		fill(b,b+10240,1);
		ans[0] = m[str[0]];
		for(int i = 0; i < len - 1; i++)
		{
			ans[i+1] = ch[ans[i]][m[str[i+1]]];
			//cout << i + 1 << ' ' << ans[i+1] << endl;
			if(ans[i+1] < 0)
			{
				ans[i+1] *= -1;
				b[i+1] = 0; 
			}
			b[i+1] ^= b[i] ;
			b[i+1] ^= 1;
		}
		/*for(int i = 0; i < len; i++)
			cout << i << ' ' << b[i] << ' ' << ans[i] << endl;*/
		bool flag = false;
		for(int i = 0; i < len && !flag; i++)
		{
			int tz = b[i];
			if(tz == 0)
				tz = -1;
			if(ans[i] * tz == 2)
			{
				for(int j = i + 1; j < len && !flag; j++)
				{
					int tx = (b[i] ^ b[j]), ty = (b[j] ^ b[len-1]);
					if(tx == 0)
						tx = -1;
					if(ty == 0)
						ty = -1;
					if(ch[ans[i]][ans[j]] * tx == 3)
					{
						if(ch[ans[j]][ans[len-1]] * ty == 4)
						{
							flag = true;
							break;
						}
					}
				}
			}
		}
		cout << "Case #" << p <<": ";
		if(flag)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	return 0;
}