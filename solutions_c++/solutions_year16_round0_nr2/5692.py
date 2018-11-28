#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>

using namespace std;

int T;

long long interpreta(long long jam, long long base)
{
	long long res = 0;
	long long a = 2;
	while(a<jam)
		a*=10;
	a/=2;
	while(a!=0)
	{
		res *= base;
		res += (jam/a)%10;
		a /= 10;
	}
	/*while(jam!=0)
	{
		res *= base;
		res += jam%10;
		jam /= 10;
	}*/
	return res;
}

long long pow(long long a, long long b)
{
	if(b==0)
		return 1;
	if(b==1)
		return a;
	long long res = pow(a,b/2);
	res *= res;
	if(b%2)
		res *= a;
	return res;
}

long long calculajam(long long n,long long asdf)
{
	long long res = 1;
	for(int i=0;i<n-2;i++)
	{
		res*=10;
		res += asdf&1;
		asdf /= 2;
	}
	res *=10;
	res++;
	return res;
}

int func(string s)
{
	vector<bool> v(s.size());
	for(int i=0;i<v.size();i++)
		v[i] = s[i]=='+';
	queue<pair<vector<bool>,int> > q;
	pair<vector<bool>,int> p,p2;
	set<vector<bool> > st;
	p.first = v;
	p.second = 0;
	q.push(p);
	while(!q.empty())
	{
		p = q.front();
		q.pop();
		if(st.find(p.first)!=st.end())
			continue;
		st.insert(p.first);
		for(int i=0;i<p.first.size();i++)
		{
			if(!p.first[i])
				goto aaa;
		}
		return p.second;
		aaa:;
		vector<bool> v2(p.first.size());
		for(int i=0;i<v2.size();i++)
		{
			for(int j=0;j<=i;j++)
				v2[j] = !p.first[i-j];
			for(int j=i+1;j<v2.size();j++)
				v2[j] = p.first[j];
			p2.first = v2;
			p2.second = p.second+1;
			q.push(p2);
		}
	}
}

int main()
{
	cin >> T;
	for(int I=0;I<T;I++)
	{
		string s;
		cin >> s;
		cout << "Case #" << I+1 << ": " << func(s) << endl;
		
	}
}
