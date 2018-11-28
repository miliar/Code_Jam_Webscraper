#include <iostream>
#include <string>
#include <vector>
using namespace std;
int num=1;
void Gao()
{
	printf("Case #%d: ",num++);
	string st;
	vector<char> a;
	int ans=0;
	char prev='_';
	cin>>st;
	for (int i=0;i<st.length();i++)
	{
		if (st[i]==prev)
		{
			continue;
		}
		else
		{
			a.push_back(st[i]);
			prev=st[i];
		}
	}
	for (int i=0;i<a.size();i++)
	{
		if (a[i]=='+')
			continue;
		if(i==0&&a[i]=='-')
		{
			ans+=1;
			continue;
		}
		if (a[i]=='-')
		{
			ans+=2;
		}
	}
	cout<<ans<<endl;
} 
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	while (T--)
		Gao();
	return 0;
}
