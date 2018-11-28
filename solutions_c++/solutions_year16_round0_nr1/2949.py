#include<bits/stdc++.h>

using namespace std;

string s;

void check(long long n,int& flag)
{
	while(n)
	{
		flag|=(1<<(n%10));
		n/=10;
	}
}

int main()
{
	int t;
	
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	cin >> t;
	
	for(int tt=0;tt<t;tt++)
	{
		int cnt=0,flag=0;
		
		long long n,num=0;
		
		cin >> n;
		
		cout << "Case #" << tt+1 << ": ";
		
		if(!n)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}
		
		while(1)
		{
			num+=n;
			
			cnt++;
			
			check(num,flag);
			
			if(flag==((1<<10)-1) || cnt==1000005)
				break;
		}
		
		if(flag==((1<<10)-1))
			cout << num << endl;
		else
			cout << "INSOMNIA" << endl;
	}
	
	return 0;
}
