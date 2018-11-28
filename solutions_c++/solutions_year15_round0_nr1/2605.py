#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int I=0;I<T;I++)
	{
		int n;
		cin >> n;
		string s;
		cin >> s;
		int res = 0;
		int lev = 0;
		for(int i=0;i<=n;i++)
		{
			int tmp = s[i]-'0';
			if(lev>=i)
				lev+=tmp;
			else
			{
				res += i-lev;
				lev = i;
				lev+=tmp;
			}
		}
		
		cout << "Case #" << I+1 << ": " << res << endl;
	}
	return 0;
}
