#include <iostream>
#include <cstring>

using namespace std;

int T,FA,SA,cnt[20];

int main()
{
	cin >> T;
	for (int i=0;i<T;i++)
	{
		memset(cnt,0,sizeof(cnt));
		cin >> FA;
		for (int line=1;line<=4;line++)
		{
			int j;
			for (int k=0;k<4;k++)
			{
				cin >> j;
				if (line==FA) cnt[j]++;
			}
		}
		cin >> SA;
		for (int line=1;line<=4;line++)
		{
			int j;
			for (int k=0;k<4;k++)
			{
				cin >> j;
				if (line==SA) cnt[j]++;
			}
		}
		int two=0;
		int card=0;
		for (int j=1;j<=16;j++)
		{
			if (cnt[j]==2)
			{
				two++;
				card=j;
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (two==1) cout << card << endl;
		else if (two>1) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}