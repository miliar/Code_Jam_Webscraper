#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#define FAST_IO ios_base::sync_with_stdio(false);//cin.tie(NULL);cout.tie(NULL);
#define MOD 1000000007  
using namespace std;

int main() 
{
	FAST_IO
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cout<<"Case #"<<t<<": ";
		int n;
		cin>>n;
		int p[n];
		int current = 0;
		for(int i=0;i<n;i++)
		{
			cin>>p[i];
			current += p[i];
		}	
		set<pair<int, int>, greater<pair<int, int> >  > s;
		for(int i=0;i<n;i++)
		{
			s.insert({p[i],i});
		}
		while(!s.empty())
		{
			auto it = s.begin();
			int x = it->first;
			int a = it->second;	
			current--;
			cout<<(char)('A'+a);
			s.erase(it);
			if(x>=2)
				s.insert({x-1,a});
			it = s.begin();
			x = it->first;
			a = it->second;
			if(2*x > current || (2*x == current && s.size()>2))
			{
				current--;
				cout<<(char)('A'+a);
				s.erase(it);
				if(x>=2)
					s.insert({x-1,a});
			} 
			cout<<" ";	
		}
		cout<<"\n";
	}
}
