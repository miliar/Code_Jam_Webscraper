#include <bits/stdc++.h>
using namespace std;
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
int main()
{
	f_in("input2.txt");
	f_out("output2.txt");
	int test;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		int N,people=0,invite_frineds=0,frineds;
		string s;
		cin>>N>>s;
		for(int i=0;i<s.size();i++)
		{
			if((s[i]-'0') && i>people)
			{
				frineds=i-people;
				people=people+frineds+(s[i]-'0');
				invite_frineds+=frineds;
			}
			else
				people=people+(s[i]-'0');
		}
		cout<<"Case #"<<t<<": "<<invite_frineds<<endl;
	}
	return 0;
}