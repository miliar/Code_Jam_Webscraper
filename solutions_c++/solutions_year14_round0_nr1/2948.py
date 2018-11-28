#include<iostream>
#include<iomanip>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
using namespace std;

int main()
{
	errno_t err1;
	errno_t err2;
	FILE *fin, *fout;
	err1 = freopen_s(&fin, "in.txt", "r", stdin);
	err2 = freopen_s(&fout, "out.txt", "w", stdout);
	int T;
	cin >> T;
	
	for (int z = 1; z <= T; ++z)
	{
		
		int c;
		cin >> c;
		set<int> s,s1;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				int x;
				cin >> x;
				if (i + 1 == c)
				{
					s.insert(x);
				}

			}
		}
		cin >> c;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				int x;
				cin >> x;
				if (i + 1 == c)
				{
					set<int>::iterator i=s.find(x);
					if (i != s.end())
						s1.insert(*(i));
				}

			}
		}
		cout << "Case #" << z << ": ";
		if (s1.size() > 1)
		{
			cout << "Bad magician!" << endl;
		}
		if (s1.size() == 1)
		{
			cout << *s1.begin() << endl;
		}
		if (s1.size() == 0)
		{
			cout <<"Volunteer cheated!"<< endl;
		}
	}
}