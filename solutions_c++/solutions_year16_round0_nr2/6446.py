#include<bits/stdc++.h>

using namespace std;

string s;
int size;
int x;
void flip(int point)
{
	if(point == 1)
	{
		if(s[0] == '-')
			s[0] = '+';
		else
			s[0] = '-';
		return;
	}
	for(int i=0;i<(point+1)/2;i++)
	{
		char c = s[i];
		if(s[point - i-1] == '-')
		{
			s[i] = '+';
		}
		else
		{
			s[i] = '-';
		}
		if(c == '-')
		{
			s[point - i-1] = '+';
		}
		else
		{
			s[point - i-1] = '-';
		}
	}
	//cout<<point<<" : "<<s<<endl;
}

int sum()
{
	int count = 0;
	int point = size;
	while(point != 0)
	{
		int pu=0, mu=0, md=0;
		while(point > 0 && s[point-1] == '+')
		{
			point--;
		}
		if(point <= 1 && s[0] == '-')
			return count+1;
		if(point <= 1 && s[0] == '+')
			return count;
		for(int i=point-1;s[i]=='-';i--)
		{
			md++;
		}
		if(s[0] == '+')
		{
			for(int i=0;i<point;i++)
			{
				if(s[i] == '+')
				{
					pu++;
				}
				else
				{
					break;
				}
			}
		}
		else
		{
			for(int i=0;i<point;i++)
			{
				if(s[i] == '-')
				{
					mu++;
				}
				else
				{
					break;
				}
			}
		}
		
				//cout<<pu<<":"<<md<<":"<<mu<<":"<<point<<endl;
				//cin>>x;
		if(pu>0)
		{
			if(pu <= md)
			{
				flip(pu);
			}
			else
			{
				flip(pu);
			}
		}
		else
		{
			if(mu > md)
			{
				flip(point);
			}
			else
			{
				flip(point);
			}
		}
		count++;
	}
	return count;
}

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		size = s.size();
		cout<<"Case #"<<i<<": "<<sum()<<endl;
	}
	return 0;
}
