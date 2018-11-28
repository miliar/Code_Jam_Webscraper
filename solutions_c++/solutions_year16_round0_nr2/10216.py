#include<bits/stdc++.h>
using namespace std;
bool check_negative(string ch)
{
	for(int i=0;i<ch.size();i++)
		if(ch[i]!='-')
			return false;
	return true;
}
int main()
{
    int t;
    cin>>t;
    int index=1;
    while(t--)
	{
		string ch;
		cin>>ch;
		if(ch.size()==1)
		{
			if(ch[0]=='-')
			{
				cout<<"Case #"<<index<<": 1\n";
				index++;
				continue;
			}
		}
        if(check_negative(ch))
		{
			cout<<"Case #"<<index<<": 1\n";
			index++;
			continue;
		}
        int ans=0;
        for(int i=0;i<ch.size()-1;i++)
		{
            if(ch[i]=='+' and ch[i+1]=='-')
				{
                    for(i=i+1;;)
					{
                        if(ch[i]=='-')
						{
							ch[i]='+';
							i++;
						}
                        else
						{
							i--;
							break;
						}
					}
					ans=ans+2;
				}
			else if(ch[i]=='-' and ch[i+1]=='+')
				{
					ans=ans+1;
                    ch[i]='+';
				}
		}
		cout<<"Case #"<<index<<": "<<ans<<"\n";
		index++;
	}
	return 0;
}
