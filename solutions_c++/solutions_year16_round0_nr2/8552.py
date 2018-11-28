#include<bits/stdc++.h>

using namespace std;

void swap(string& s, int pos)
{
	int i;
	for(i=0;i<= pos;i++)
	{
		if( s[i] == '-' )
			s[i] = '+';
		else
			s[i] = '-';
	}
}

int findLastN(string s,int lastN)
{
	
	int i;
	for(i= lastN;i>=0;i--)
	{
		if( s[i] == '-' )
			break;
	}
	return i;
}

int main(void)
{
	int t,te;
	cin>>te;
	string s;
	int res;
	for(t=1;t <= te ;t++)
	{
		cin>>s;
		printf("Case #%d: ",t);
		res = 0;
		int len = s.size();
		int i,nPos;
		bool nFound = false;
		for(i = len - 1 ; i >= 0 ;i-- )
		{
			if( s[i] == '-' )
			{
				nFound = true;
				break;
			}
		}
		if( nFound )
		{
			nPos = i;
			if( nPos == 0 )	
			{
				cout<<"1\n";
			}
			else
			{
				int lastn = nPos;
				while( nPos != -1 )	
				{
					res++;
					for(i= lastn ; i>=0 ;i--)
					{
						if( s[i] == '-' && s[0] == '+')
							continue;
						swap(s,i);
						break;
					}
					nPos = findLastN(s,nPos);
				}
				cout<<res<<endl;
			}
		}	
		else
		{
			cout<<"0\n";
		}
	}
	return 0;
}
