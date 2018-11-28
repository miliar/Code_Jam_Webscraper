#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,j,k,l,c,p=1;
	string s;
	cin >> t;
	while(t--)
	{
		cin >> s;c=0;
		for(i=s.size()-1;i>=0;i--)
		{
			if(s[i]=='-')
			{
				for(j=i;j>=0;j--)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				c++;
			}
		}
		cout << "Case #" << p << ": " << c << endl;
		p++;
	}
}

