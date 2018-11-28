#include <bits/stdc++.h>
typedef long long int ll;
#define fio ios_base::sync_with_stdio(false)
using namespace std;

void genString(vector<string>& v, string s,int digitsLeft)
{
	if(digitsLeft == 1) // the length of string is n
      v.push_back(s+"1");
	else
   	{
    	genString( v,s + "0", digitsLeft - 1 );
    	genString( v,s + "1", digitsLeft - 1 );
   	}
}

ll isPrime(ll num)
{
	if(num%2==0) return 2;
	for(int i=3;i<=sqrt(num);i+=2)
		if(num%i==0) 
			return i;
	return 0;
}

ll convert(string s,ll num)
{
	ll ans=0,mul=1;
	for(int i=s.size()-1;i>=0;i--)
	{
		ans += mul*(s[i]-'0');
		mul *= num;
	}
	return ans;
}

int main() {
	fio;
	ll t,n,j;
	cin>>t>>n>>j;
	cout<<"Case #1:\n";
	vector<string> v;
	genString(v,"1",15);
	int out=0;
	for(auto it=v.begin();out<50 && it!=v.end();it++)
	{
		int flag=0;
		vector<ll> ans;
		for(int i=2;flag==0 && i<=10;i++)
		{
			ll ch = convert(*it,i);
			ll di = isPrime(ch);
			if(di) ans.push_back(di);
			else flag++;
		}
		if(flag==0)
		{
			cout<<*it<<" ";
			for(auto it1=ans.begin();it1!=ans.end();it1++)
				cout<<*it1<<" ";
			cout<<"\n";
			out++;
		}
	}
	return 0;
}