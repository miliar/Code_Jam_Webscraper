#include <bits/stdc++.h>

using namespace std;

map<pair<int,int>,int> m;

int get(char x)
{
	if(x=='1')
		return 1;
	else if(x=='i')
		return 2;
	else if(x=='j')
		return 3;
	else if(x=='k')
		return 4;
	return -1;
}

void init()
{
	m[{1,1}] = 1;
	m[{1,2}] = 2;
	m[{1,3}] = 3;
	m[{1,4}] = 4;
	m[{2,1}] = 2;
	m[{2,2}] = -1;
	m[{2,3}] = 4;
	m[{2,4}] = -3;
	m[{3,1}] = 3;
	m[{3,2}] = -4;
	m[{3,3}] = -1;
	m[{3,4}] = 2;
	m[{4,1}] = 4;
	m[{4,2}] = 3;
	m[{4,3}] = -2;
	m[{4,4}] = -1;
}

int power(int a,int b)
{
	if(b==0)
		return a;
	if(a==1)
		return 1;
	if(a==-1) {
		if(b&1)
			return -1;
		return 1;
	}
	if(b%4==0)
		return 1;
	else if(b%4==1)
		return a;
	else if(b%4==2)
		return -1;
	else
		return -a;
}

int main()
{
	init();
	int t;
	cin>>t;
	for (int T = 1; T <= t; ++T) {
		string s;
		int l,x,p=1;
		cin>>l>>x;
		cin>>s;
		for (int i = 0; i < s.size(); ++i) {
			if(p<0)
				p = -m[{-p,get(s[i])}];
			else
				p = m[{p,get(s[i])}];
			// P[i] = p;
			// cout<<P[i]<<endl;
		}

		// cout<<p<<endl;

		if(power(p,x)!=-1) {
			printf("Case #%d: NO\n",T);
			continue;
		}

		for(int i=0;i<min(4,x);i++){
			s+=s;
		}

		p=1;
		bool flag = false;
		for (int i = 0; i < s.size(); ++i) {
			if(p<0)
				p = -m[{-p,get(s[i])}];
			else
				p = m[{p,get(s[i])}];
			// cout<<"p:"<<p<<endl;
			if(p==get('i')) {
				int q=1;
				// cout<<"i:"<<i<<endl;
				for (int j = i+1; j < s.size(); ++j) {
					if(q<0)
						q = -m[{-q,get(s[j])}];
					else
						q = m[{q,get(s[j])}];
					// cout<<"q:"<<p<<endl;
					if(q==get('j')){
						flag = true;
						break;
					}
				}
			}
			if(flag)
				break;
		}
		if(flag) 
			printf("Case #%d: YES\n",T);
		else
			printf("Case #%d: NO\n",T);
	}
}