#include<iostream>
#include<vector>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	long long n;
	string s;
	int Case=1;
	while(t--)
	{
		cin>>s;
		n=0;
		int pos  = s.find_last_of('-');
		while(pos!=-1)
		{
			for(int i=0;i<=pos;i++)
			{
				if(s[i]=='+')
				s[i]='-';
				else
				s[i]='+';
			}
			pos=s.find_last_of('-');
			n++;
		}
		cout<<"Case #"<<Case<<": "<<n<<endl;
		Case++;
	}
	return 0;
}
