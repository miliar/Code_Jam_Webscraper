#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip> 
#include <cmath>
#include <string>
using namespace std;


//p -> 0
//r -> 1
//s -> 2

string result;
int n;

bool match(string&S)
{
	vector<int> a; vector<int> b;
	for(int i=0; i<n; i++)
		a.push_back(S[i]);

	while(a.size() != 1)
	{
		for(int i=0; i<a.size() -1 ; i+=2)
		{
			if(a[i] == a[i+1])
				return false;

			if( (a[i] == '0' && a[i+1] == '1') || (a[i] == '1' && a[i+1] == '0'))
				b.push_back('0');

			if( (a[i] == '1' && a[i+1] == '2') || (a[i] == '2' && a[i+1] == '1'))
				b.push_back('1');

			if( (a[i] == '0' && a[i+1] == '2') || (a[i] == '2' && a[i+1] == '0'))
				b.push_back('2');

		}

			a.swap(b);
			b.clear();
	}
	return true;
}


void f(int p, int r, int s, string& S, int ix)
{
	// cerr<<p<<" "<<r<<" "<<s<<" "<<S<<" "<<ix<<endl;
	if(p==0 && r==0 && s==0)
	{
		if( S < result)
		{
			if(match(S))
				result = S;
		}
		return;
	}

	if(p != 0)
	{
		S[ix] = '0';
		f(p-1, r, s, S, ix+1);
	}

	if(r != 0)
	{
		S[ix] = '1';
		f(p, r-1, s, S, ix+1);
	}

	if(s != 0)
	{
		S[ix] = '2';
		f(p, r, s-1, S, ix+1);
	}


}

int main()
{

	int zz; cin>>zz;
	for(int i_=1; i_<=zz; i_++)
	{
		result = "999";
		int r,p,s;
		cin>>n>>r>>p>>s;
		n = 1<<n;
		string S;
		S.resize(n);
		for(int i=0; i<n; i++)
			S[i] = '9';
		f(p, r, s, S, 0);

		if(result == "999")
			cout<<"Case #"<<i_<<": "<<"IMPOSSIBLE"<<endl;
		else{
			cout<<"Case #"<<i_<<": ";
			for(int i=0; i<result.size(); i++)
			{
				if(result[i] == '0')
					cout<<"P";
				if(result[i] == '1')
					cout<<"R";
				if(result[i] == '2')
					cout<<"S";
				
			}
			cout<<endl;

		}

	}
}


//p -> 0
//r -> 1
//s -> 2