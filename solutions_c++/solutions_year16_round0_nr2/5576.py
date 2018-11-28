#include<iostream>
#include<queue>
using namespace std;
bool check(string &str)
{
	bool ans = true;
	for(int i=0;i<str.size();i++)
	{
		if(str[i] == '-')
			return false;
	}
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int k = 1;
	while(t--)
	{
		cout<<"Case #"<<k++<<": ";
		string str;
		cin>>str;
		int ans = 0;
		while(!check(str))
		{
			ans++;
			int i;
			for(i=1;i<str.size() && str[i] == str[i-1];i++);
				for(int j=0;j<i;j++)
				{
					str[j] = (str[j] == '-' ? '+' : '-');
				}
		}
		cout<<ans<<endl;
	}
	return 0;
}