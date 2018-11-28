#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int t,count(1);
	cin>>t;
	char s[1005];
	cin.getline(s,1,'\n');	//for neglecting the "\n" after testcase input.
	while(count<=t)
	{
		cin.getline(s,1005,'\n');
		int i=1;
		while(s[i]!='\0')
		{
			if(s[i]>=s[0])
			{
				char t = s[i];
				for(int j=i;j>0;j--)
				{
					s[j]=s[j-1];
				}
				s[0]=t;
				i++;
			}
			else
			i++;
		}
		string ans = s;
		cout<<"Case #"<<count<<": "<<ans<<endl;
		count++;
	}
}
