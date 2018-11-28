#include<iostream>
using namespace std;
#define ull unsigned long long
char arr[2]={'-','+'};
int main()
{
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		string s;
		cin>>s;
		int ans=0;
		int curr=0;
		for(int i=s.length()-1;i>=0;)
		{
			int did=0;
			while(i>=0 && s[i]==arr[curr])
			{
				did=1;
				i--;
			}
			ans+=did;
			if(did)
			{
				curr++;curr%=2;
			}
			while(i>=0 && s[i]!=arr[curr])
			{
				i--;
			}
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
	return 0;
}
