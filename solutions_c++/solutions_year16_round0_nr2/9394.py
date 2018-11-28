#include <bits/stdc++.h>

using namespace std;

int main()
{
	int end;
	int i,j,n,t;
	cin >> t;
	string s;
	for(int k=1; k<=t; k++)
	{
		cin >> s;
		char* temp = new char[s.length()];
		bool isMinus;
		int cnt = 0;
		end = s.length()-1;
		while(1)
		{
			
			isMinus = false;
			for(i=end; i>=0; i--)
			{
				if(s[i]=='-')
				{
					end = i;
					isMinus = true;
					break;
				}
			}

			if(!isMinus)
				break;
			else
			{
				i = 0;
				while(1)
				{
					if(s[i]=='+')
					{
						s[i] = '-';
						i++;						
					}
					else
					{
						break;
					}
				}
				if(i>0)
					cnt++;
				for(i=0; i<=end; i++)
				{
					temp[end-i] = s[i];
				}
				for(i=0; i<=end; i++)
				{
					if(temp[i]=='-')
						s[i] = '+';
					else
						s[i] = '-';
				}
				cnt++;
			}

		}
		cout << "Case #" << k << ": " << cnt << endl;
	}
} 