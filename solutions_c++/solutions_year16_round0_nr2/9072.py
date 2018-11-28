#include<bits/stdc++.h>
#define ll long long int
using namespace std;

string revers(string s,ll index)
{
	string b="";
	for(ll i=index;i>-1;--i)
		b=b+s.at(i);
	
	for(ll i=0;i<b.length();++i)
{
		if(b.at(i)=='-')
			b.at(i)='+';
	else
			b.at(i)='-';

}
	for(ll i=index+1;i<s.length();++i)
		b+=s.at(i);
	return b;
	
}

int main()
{
	ll test;
	
	cin >> test;
	ll t=test;
	while(test--)
{
	ll cnt=0;
	string s;
	cin >> s;
	ll st=0;
	ll en=s.length()-1;
	while(en>=0)
{
	st=0;
	if(s.at(en)=='+')
		--en;
	else
{
	ll temp1,temp2,temp3;
	if(s.at(st)=='+')
	{
		temp1=st;
		while(s.at(st)=='+')
			++st;
		s=revers(s,st-1);
		++cnt;
	}
	else
	{
		ll num1=0;
		ll num2=0;
		temp1=en;
		temp2=st;
		//cout << "ffs";
				while(temp1>=0&&s.at(temp1)=='-')
		{
					++num1;
					--temp1;
		}
				while(temp2<s.length()&&s.at(temp2)=='-')
		{
					++num2;
					++temp2;
		}
		//cout << num1 << num2 << "\n";
		if(num1==num2)
			{
				++cnt;
				s=revers(s,num2-1);
				
			}
		else if(num1>num2)
		{
			s=revers(s,num2-1);
			++cnt;
		}
		else
		{
			s=revers(s,en);
			++cnt;
		}

	}

}


}
	cout <<  "Case #" << t-test << ": "<<cnt << "\n";
}
	
}


