#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int qq = 1; qq <= t; ++qq)
	{
		int n;
		scanf("%i",&n);
		vector <int> v(n+1);
		char cc[1050]="\0";
		char c;
		scanf("%s",cc);
		for (int i = 0; i < n+1; ++i)
		{
			v[i]=int(cc[i]) - 48;
		}
		int st=0,diff=0;
		for (int i = 0; i < n+1; ++i)
		{
			if(st>=i){
				st+=v[i];
			}
			else{
				diff+=i-st;
				st+=i-st;
//				assert(st==i);
				st+=v[i];
			}
		}
		printf("Case #%i: %i\n",qq, diff);
	}
	return 0;
}