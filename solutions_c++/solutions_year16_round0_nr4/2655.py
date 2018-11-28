#include<iostream>
#include<string>
#include<cmath>
#include<cstdio>
using namespace std;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w+",stdout);
	long long int cases,caseno=1;
	cin>>cases;
	while(cases--)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout << "Case #" << caseno++ << ": ";
		for(int i=1;i<=s;i++)
			cout << i << " ";
		cout << "\n";
	}
	return 0;
}
