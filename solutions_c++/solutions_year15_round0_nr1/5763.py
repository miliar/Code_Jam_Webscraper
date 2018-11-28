#include <string>
#include <cstdio>
#include <iostream>

#define FILE_NAME "data"

using namespace std;

char buffer[256];

int main()
{
	int case_num, i, ans, sum, temp;

	sprintf(buffer, "%s.in", FILE_NAME);
	freopen(buffer, "r", stdin);
	sprintf(buffer, "%s.out", FILE_NAME);
	freopen(buffer, "w", stdout);

	cin>>case_num;
	i=0;
	while(i<case_num)
	{
		
		string input;
		cin>>temp>>input;
		ans = 0;
		sum = 0;
		for(int j=0;j<input.length();j++)
		{
			int val = input[j]-'0';
			if(val==0)
				continue;
			
			if(sum>=j)
				sum+=val;
			else
			{
				ans+=j-sum;
				sum+=j-sum;
				sum+=val;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		i++;
	}
		
	return 0;
}