#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main()
{
	ll n, i, t;
	cin >> t;
	for(ll j=0; j<t; j++)
	{
		cin >> n;
		int arr[10];
		for(i=0; i<10; i++)
		{
			arr[i] = 0;
		}
		ll p = n;
		int count = 2;	
		while(true)
		{
			if(n == 0)
			{
				cout << "Case #"<< (j+1) <<": INSOMNIA"<<'\n';
				break;
			}
			int check=0;					
			string s = to_string(p);
			//cout << s << '\n';
			for(i=0; i<s.length(); i++)
			{
				int a =  s.at(i)-'0';
				//cout << a << "jj\n";
				if(!arr[a])
				{
					arr[a] = 1;
				}
			}
			for(i=0; i<10; i++)
			{
				
				if(arr[i] == 0)
				{
					check = 1;
					break;
				}
			}
			if(!check)
			{
				break;
			}
			p = count * n;
			count++;
		}
		if(n!=0)
			cout << "Case #"<< (j+1) <<": "<< p <<'\n';
	}
}