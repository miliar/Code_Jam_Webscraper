/**************************************************
**  Author:  Aditya Goel                          *
**  NIT, Kurukshetra                              *  
**  INDIA                                         * 
**************************************************/

#include<bits/stdc++.h>
using namespace std;
//#define S second
#define sd(mark) scanf("%d",&mark)

int main()
{
	freopen("inl1.txt", "r", stdin);
	freopen("outl1.txt", "w", stdout);
	int test;
	sd(test);
	for(int tt = 1; tt <= test; tt++)
	{
		string s;
		cin >> s;
		string res;
		
		for(int i = 0; i < s.length(); i++)
		{
			if(res.empty())
			{
				res.insert(res.begin(), s.at(0));
			}
			else
			{
				if(res.at(0) > s.at(i))
				{
					res.insert(res.end(), s.at(i));
				}
				else
				{
					res.insert(res.begin(), s.at(i));
				}
			}
		}
		printf("Case #%d: ", tt);
		cout << res << "\n";
	}
	return 0;
}
