#include <iostream>
#include <string.h>
#include <string>

using namespace std;

int shy[1001];
int max_level;

int main(int argc, char *args[])
{
	 
        freopen("A-small-attempt2.in","rt",stdin);
        freopen("A-small-attempt2.out","wt",stdout);

	int t;
	cin>>t;
	int count = 1;
	while(t--)
	{
		memset(shy, 0, sizeof(shy));
		string s;
		cin>>max_level;
		cin>>s;
		for(int i = 0; i < s.size(); ++i)
			shy[i] = s[i] - '0';

		int answer = 0;
		int now = shy[0];
		for(int i = 1; i < max_level + 1; ++i)
		{
			if(now > max_level) break;
			if(shy[i] == 0) continue;
			if(now < i)
				{
					answer+=(i - now);
					now += answer;
			}
			now += shy[i];
		}
		printf("Case #%d: %d\n", count, answer);
		count++;
	}
}