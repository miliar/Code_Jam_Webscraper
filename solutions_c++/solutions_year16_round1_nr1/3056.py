#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("cj_q1_l.out","w",stdout);
	int t;
	cin>>t;
	int k=0;
	while(t--)
	{
		k++;
		string s;
		cin>>s;
		int l=s.length();
		char c=s[0];
		string s1="";
		s1=s1+c;
		for(int i=1;i<l;i++)
		{
			if(s[i]>=s1[0])
			{
				s1=s[i]+s1;
			}
			else
			{
				s1=s1+s[i];
			}
		}
		cout<<"Case #"<<k<<": "<<s1<<endl;
	}
	return 0;
}
