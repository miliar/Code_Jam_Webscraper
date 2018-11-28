#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t, count;
    bool allAreHappy, allAreBlank;
    string s;
    ofstream file;
    file.open("B-large.o");

    cin>>t;
	for(int i = 0; i < t; i++)
	{
		cin>>s;
		count = 0;
		allAreHappy = false;
		allAreBlank = false;
		int pos = s.find_first_not_of(s[0]);
		if(pos == string::npos)
		{
			if(s[0] == '+')
			{
				allAreHappy = true;
			}
			else if(s[0] == '-')
			{
				allAreBlank = true;
			}
		}
		if(allAreBlank)
		{
			cout<<"Case #"<<i+1<<": 1"<<endl;
			file<<"Case #"<<i+1<<": 1"<<endl;
		}
		else if(allAreHappy)
		{
			cout<<"Case #"<<i+1<<": 0"<<endl;
			file<<"Case #"<<i+1<<": 0"<<endl;
		}
		else
		{
			while(pos != string::npos)
			{
                if(s[0] == '-')
				{
					for(int j = 0; j < pos; j++)
					{
						s[j] = '+';
					}
				}
				else if(s[0] == '+')
				{
					for(int j = 0; j < pos; j++)
					{
						s[j] = '-';
					}
				}
				count++;
				pos = s.find_first_not_of(s[0]);
			}
			if(s[0] == '-')
			{
				count++;
			}
			cout<<"Case #"<<i+1<<": "<<count<<endl;
			file<<"Case #"<<i+1<<": "<<count<<endl;
		}
	}

	file.close();
	return 0;
}
