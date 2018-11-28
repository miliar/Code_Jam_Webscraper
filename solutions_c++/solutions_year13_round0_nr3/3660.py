#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<sstream>

using namespace std;

#define ll long long


string ll_to_string ( ll num )
{
	stringstream A;
	A << num;
	return (A.str());
}

ll is_a_palindrome ( ll num )
{
	ll flag = 1;
	string str = ll_to_string(num);
	string::iterator iter_begin = str.begin() ;
	string::iterator iter_end = str.end() - 1;

	for (; iter_begin < iter_end; iter_begin++, iter_end-- )
	{
		flag = 1;
		if ( *iter_begin != *iter_end )
		{
			flag = 0;
			break;
		}
	}
	return flag;
}


int main()
{
	ll t;
	cin>>t;

	for(ll i=0;i<t;i++) {
		ll a,b;
		cin>>a>>b;
		ll result=0;
		ll start=sqrt(a);
		for(ll j=start;j<sqrt(b)+1;j++) {
			if(j*j>=a && j*j<=b)
			if(is_a_palindrome(j*j) && is_a_palindrome(j))
				//cout<<j*j<<" "<<j<<"\n";
				result++;
		}
		cout<<"Case #"<<i+1<<": "<<result<<"\n";	
	}
	return 0;
}