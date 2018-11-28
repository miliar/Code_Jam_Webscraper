#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ull;



void test()
{
	ull k, c, s;
	cin>>k>>c>>s;
	if (s < k)
	{
		cout<<"IMPOSSIBLE\n";
		return;
	}
	for(int i=1; i<=k; i++)
		cout << i << " ";
	
	cout << "\n";
}

int main()
{
	int testy;
	cin>>testy;
	for(int i=1; i<=testy; i++)
	{
		cout << "Case #"<<i<<": ";
		test();
	}
}

