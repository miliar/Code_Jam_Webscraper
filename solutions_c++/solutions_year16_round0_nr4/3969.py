#include<bits/stdc++.h>
using namespace std;

ifstream goo;
ofstream gle;

void solve()
{
	int k,c,s;
	long long a=1,l=1;
	goo>>k>>c>>s;
	if(s<k) gle<<"IMPOSSIBLE";
	else for(int i=1; i<=k; i++) gle<<i<<" ";
	gle<<"\n";
	return;
}

int main()
{
	int t;
	ios_base::sync_with_stdio(0);
   	goo.open("C:\\Users\\Mateusz\\Downloads\\D-small-attempt5.in");
   	//goo.open("C:\\Users\\Mateusz\\Desktop\\goo.in");
   	gle.open("C:\\Users\\Mateusz\\Desktop\\gle.out");
	goo>>t;
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<": ";
		solve();
	}
	goo.close();
	gle.close();
	return 0;
}
