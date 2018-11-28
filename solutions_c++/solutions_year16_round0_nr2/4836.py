#include <bits/stdc++.h>
using namespace std;
int main()
{
	int i, t, j, head, tail, k, Count, cc;
	string s, s1;
	cin>>t;
	cc=1;
	while(t--)
	{
		cin>>s;
		//cout<<"s: "<<s<<endl;
		Count=0;
		head=0;
		tail=s.length()-1;
		while(tail>=0)
		{
			if(s[tail]=='+' && tail>=0)
			{
				tail--;
			}
			else if(s[tail]=='-' && s[0]=='-')
			{
				// invert the string
				j=0;
				for(i=tail; i>=0; i--)
				{
					if(s[i]=='+')
						s1[j]='-';
					else
						s1[j]='+';
					j++;
				}
				for(i=0; i<=tail; i++)
					s[i]=s1[i];
				Count++;
			}
			else if(s[tail]=='-' && s[0]=='+')
			{
				j=0;
				while(s[j]=='+' && j<=tail)
				{
					j++;
				}

				k=0;
				for(i=j-1; i>=0; i--)
				{
					if(s[i]=='+')
						s1[k]='-';
					else
						s1[k]='+';
					k++;
				}
				Count++;
				for(i=0; i<=j-1; i++)
					s[i]=s1[i];
			}
			//cout<<"S: "<<s<<endl;
		}

		cout<<"Case #"<<cc<<": "<<Count<<endl;
		cc++;
	}
	return 0;
}