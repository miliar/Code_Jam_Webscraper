#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int c = 1;
	while(c <= t)
	{
		string s;
		cin>>s;
		int cnt = 0,opr = 0;
		for(int i=0;i<s.size();i++)
		{
				if(s[i]=='+')
					cnt++;
		}
		if(cnt==s.size())
		{
				cout<<"Case #"<<c<<": "<<opr<<endl;
		}
		else
		{

				while(1)
				{
						string ss;
						char c = s[0];
						int l = 0;
						while((l < s.size()) && (s[l]== c))
						{
								if(s[l]=='+')
									ss += '-';
								else
									ss += '+';
								l++;
						}
						int sz = ss.size();
						for(int j=0;j < sz;j++)
								s[sz-1-j] = ss[j];
						//cout<<ss<<endl;
						int plus_cnt = 0;
						for(int i=0;i<s.size();i++)
						{			
							if(s[i]=='+')
								plus_cnt++;
						}
						opr++;
						//cout<<s<<endl;
						if(plus_cnt == s.size())
								break;	
						//ss.clear();
				}
				
					cout<<"Case #"<<c<<": "<<opr<<endl;	
		}
	
		c++;	
	}
}
