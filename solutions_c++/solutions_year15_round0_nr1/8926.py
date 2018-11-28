#include<iostream>
using namespace std;

int main()
{
	int t, s, test, friends, audCount, smax, audience[1002];
	char str[1002];
	
	cin >> t;
	test = t;
	
	while(t--)
	{
		cin >> smax;
		cin >> str;
		
		friends = 0;
		audCount = 0;
		
		for(s = 0; s <= smax; s++)
		{
			audience[s] = str[s] - 48;
			
			if(s > 0 && audCount < s && audience[s] > 0)
			{
				friends += s - audCount;
				audCount += s - audCount;
			}
			
			audCount += audience[s];
		}
		
		cout << "Case #" << test-t << ": " << friends << endl;
	}
	return 0;
}
