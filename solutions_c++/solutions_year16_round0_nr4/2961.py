#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <string>
#include <math.h>
using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	for (int l = 0; l < t; ++l)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<l+1<<": ";
		for (int i = 1; i <= s; ++i)
			cout<<i<<" \n"[i == s];
	}
	return 0;
}