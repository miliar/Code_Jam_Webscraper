#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define FORI(i,b,a) for(int i=b;i>=a;--i)

bool mark(long long int curr, bool seen[])
{
	while(curr !=0)
	{
		seen[(curr%10)] = true;
		curr = curr/10;
	}
	FOR(i,0,10)
	{
		if(!seen[i])return false;
	}
	return true;

}

int main()
{
	int t;
	cin>>t;
	FOR(casenum,1,t+1)
	{
		int n;
		cin>>n;
		if(!n){
			cout<<"Case #"<<casenum<<": INSOMNIA"<<endl;
			continue;
		}
		bool seen[10];
		bzero(seen, 10*sizeof(bool));
		long long int i=1;
		long long int curr;
		while(true)
		{
			curr= n*i;
			if(mark(curr, seen))
			{
				cout<<"Case #"<<casenum<<": "<<curr<<endl;
				break;
			}
			++i;
		}
	}
}