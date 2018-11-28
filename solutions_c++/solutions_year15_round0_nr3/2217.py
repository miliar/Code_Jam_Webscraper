#include <bits/stdc++.h>
using namespace std;

map<char,map<char,pair<char,bool> > > T;

int main()
{
	T['1']['1'].first = '1';
	T['1']['i'].first = 'i';
	T['1']['j'].first = 'j';
	T['1']['k'].first = 'k';
	T['i']['1'].first = 'i';
	T['i']['i'].first = '1';
	T['i']['i'].second = true;
	T['i']['j'].first = 'k';
	T['i']['k'].first = 'j';	
	T['i']['k'].second = true;	
	T['j']['1'].first = 'j';	
	T['j']['i'].first = 'k';	
	T['j']['i'].second = true;	
	T['j']['j'].first = '1';	
	T['j']['j'].second = true;	
	T['j']['k'].first = 'i';	
	T['k']['1'].first = 'k';	
	T['k']['i'].first = 'j';	
	T['k']['j'].first = 'i';	
	T['k']['j'].second = true;	
	T['k']['k'].first = '1';	
	T['k']['k'].second = true;		
	int t,l;
	long long x,rot;
	string s;
	cin >> t;
	for(int test=1;test<=t;++test)
	{
		cin >> l >> x;
		cin >> s;
		char res = '1';
		bool neg = false;
		for(int i=0;i<s.size();++i)
		{
			neg ^= T[res][s[i]].second;
			res = T[res][s[i]].first;
		}
		if(neg && res=='1')
			rot = 2;
		else if(!neg && res=='1')
			rot = 1;
		else
			rot = 4;
		long long rep = min(12LL,x);
		string w;
		bool solved = false;
		for(int i=0;i<rep && !solved;++i)
		{
			w += s;
			int state = 0;
			res = '1';
			neg = false;
			for(int j=0;j<w.size();++j)
			{
				neg ^= T[res][w[j]].second;
				res = T[res][w[j]].first;
				if(state==0 && !neg && res=='i')
					state = 1;
				else if(state==1 && !neg && res=='k')
					state = 2;
			}
			if(state==2 && neg && res=='1')
				state = 3;
			if(state==3)
			{
				long long left = x-i-1;
				if(left%rot==0)
					solved = true;
			}
		}
		cout << "Case #" << test << ": ";
		if(solved)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	return 0;
}
