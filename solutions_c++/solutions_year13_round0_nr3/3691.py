#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
using namespace std;
bool palin(int n)
{
	int cn = n;
	int y = 0;	
	while(n)
	{
		y = y*10 + n%10;
		n/=10;
	}
	return cn == y;
}
int main()
{
	int t;
	cin >> t;
	for(int k = 1;k<=t;k++)
	{
		int a,b;
		int cnt = 0;
		cin >> a >> b;
		for(int i = 1; i*i <= b;i++)
		{
			if(palin(i))
			{
				long long j = i*i;
				if(j >=a && j <= b && palin(j))
				{
					//cout << i << " " << j << endl;					
					cnt++;
				}
			}
		}
		cout << "Case #"<<k <<": "<< cnt << endl;
	}	
}
