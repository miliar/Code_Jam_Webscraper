#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i=1; i<=t; i++)
	{
		string s;
		int arr[100],count=0;
		cin >> s;
		for(int j=s.length()-1; j>=0; j--)
		{
			if(s[j]=='+')
			{
				arr[s.length()-1-j] = 1;
			}
			else if(s[j]=='-')
			{
				arr[s.length()-1-j] = 0;
			}
		}
		for(int j=0;j<s.length();j++)
		{
			if(arr[j]==0)
			{
				count+=1;
				for(int k=j; k<s.length(); k++)
				{
					arr[k] = (arr[k]+1)%2;
				}
			}
		}
		cout << "Case #" << i <<": " << count <<endl;
	}
	return 0;
}