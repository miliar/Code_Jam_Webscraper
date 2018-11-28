#include <iostream>
#include <fstream>

using namespace std;

ofstream fout("file.out");

int t,a,b,c,ans;

int main()
{
	cin >> t;
	
	for (int i = 0; i < t; i++)
	{
		cin >> a >> b >> c;
		
		for (int h = 0; h < a; h++)
		{
			for (int j = 0; j < b; j++)
			{
				int l = (h&j);
				
				if (l < c) ans++;
			}
		}
		
		fout << "Case #" << i+1 << ": " << ans << "\n";
		
		ans = 0;
	}
}
