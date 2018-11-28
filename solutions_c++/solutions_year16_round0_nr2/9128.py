#include<iostream>
#include<string>
using namespace std;

int main()
{
	int t;
	cin >> t ;
	char prev;
	for(int i=1;i<=t;i++)
	{
		string str;
		cin >> str;
		int cnt = 0,l,j;
		l = str.length();
		j=1;
		prev = str[0];
		while(j<l)
		{
			while(str[j]==prev&&j<l)
			{
				j++;
			}
			if(prev=='-')
			{
				cnt = cnt+1;
				prev = '+';
			}
			else if(prev=='+'&&j<l)
			{
				cnt+=1;
				prev = '-';
			}

		}
		if(prev=='-')
			cnt++;
		cout << "Case #" << i << ": "<<cnt <<endl;
	}
	return 0;
}