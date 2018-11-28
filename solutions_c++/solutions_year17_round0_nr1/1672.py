#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int gh=1;gh<=t;gh++)
	{
		string s;
		int k;
		cin>>s>>k;

		int answer = 0;

		int *flipped = new int[s.length()];
		for(int i=0;i<s.length();i++)
			flipped[i]=0;

		for(int i=s.length()-1;i>=0;i--)
		{

			int numFlipped = 0;
			for(int j=i+1;j<(i+k) && j<s.length();j++)
			{
				numFlipped+=flipped[j];
			}

			if(numFlipped%2!=0)
			{
				if(s[i]=='+')
					s[i]='-';
				else
					s[i]='+';
			}

			if(i>=(k-1))
			{
				if(s[i]=='-')
				{
					flipped[i] = 1;
					s[i]='+';
					answer++;
				}
				else
				{
					flipped[i] = 0;
				}
			}
		}

		bool poss = true;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				poss=false;
				break;
			}
		}

		if(poss)
			cout<<"Case #"<<gh<<": "<<answer<<endl;
		else
			cout<<"Case #"<<gh<<": "<<"IMPOSSIBLE"<<endl;
	}
}