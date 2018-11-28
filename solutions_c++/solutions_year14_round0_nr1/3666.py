#include<iostream>
#include<cstring>

using namespace std;

int a1[16];
int a2[16];
bool v[17];
int main()
{
	int nCase;
	cin >> nCase;
	int r1, r2, offset;
	int repeat, lastRepeat;
	for (int z = 1; z <= nCase; ++z)
	{
		cin >> r1;
		for (int i = 0; i < 16; ++i)
			cin >> a1[i];
		cin >> r2;
		for (int i = 0; i < 16; ++i)
			cin >> a2[i];
		
		memset(v, 0, sizeof(v));
		offset = (r1 - 1) * 4;
		for (int i = 0; i < 4; ++i)
			v[a1[offset + i]] = true;
		offset = (r2 - 1) * 4;
		repeat = 0;
		for (int i = 0; i < 4; ++i)
		{
			if (v[a2[offset + i]])
			{
				++repeat;
				lastRepeat = a2[offset + i];
			}
			v[a2[offset + i]] = true;
		}
		cout << "Case #" << z << ": ";
		if (repeat == 0)
			cout << "Volunteer cheated!" << endl;
		else if (repeat == 1)
			cout << lastRepeat << endl;
		else
			cout << "Bad magician!" << endl;
			

	}
	return 0;
}