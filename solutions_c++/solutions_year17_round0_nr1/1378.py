#include<cstdio>
#include<string>
#include<iostream>

using namespace std;
		
int main()
{
	int t;
	scanf("%d", &t);
	bool flipChange[1001];
	for(int tt = 1; tt <= t; tt++)
	{
		string s;
		int k;
		cin >> s;
		scanf("%d", &k);
		for(int i = 0; i < s.length(); i++)
			flipChange[i] = false;
		int count = 0;
		bool faceUp = true;
		for(int i = 0; i < s.length(); i++)
		{
			if(flipChange[i])
				faceUp = !faceUp;
			if((s[i] == '+' && !faceUp) || (s[i] == '-' && faceUp))
			{
				int flipIdx = i + k;
				if(flipIdx > s.length())
				{
					count = -1;
					break;
				}
				count++;
				faceUp = !faceUp;
				flipChange[flipIdx] = true;
			}
		}
		printf("Case #%d: ", tt);
		if(count == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", count);
	}
	return 0;
}

