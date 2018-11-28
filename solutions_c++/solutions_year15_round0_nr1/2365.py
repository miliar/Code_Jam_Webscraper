#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	int T;
	int tmp[1010];
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	while(cin >> T)
	{
		for(int j = 1; j <= T; j++)
		{
			
			int maxs;
		 	cin >> maxs;
		 	//cout << maxs << ":";
			int sum = 0, rst = 0;
			char tmps;
			getchar();
			for(int i = 0; i <= maxs; i++)
	 		{
	 			cin >> tmps;
	 			tmp[i] = tmps - '0';
 			 	//cout << tmp[i];
	 		}
	 		//cout << ":";
	 		if(maxs == 0)
	 		{
	 			cout << "Case #" << j << ": ";
	 				cout << 0 << endl;
		 		continue;
		 	}
		 	for(int i = 1; i <= maxs; i++)
		 	{
	 			sum += tmp[i-1];
	 			if(sum < i)
	 			{
	 				rst++;
	 				sum++;
	 			}
	 		}
	 		cout << "Case #" << j << ": " << rst << endl;
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
