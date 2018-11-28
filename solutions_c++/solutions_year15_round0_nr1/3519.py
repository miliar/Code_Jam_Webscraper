#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	int i;
	for (i=0; i<t; i++)
	{
		int smax;
		scanf("%d",&smax);
		char string[smax + 2];
		scanf("%s",string);
		int j,currstanding = 0, currlevel= 0, required = 0;
		for(j=0; j<smax+1; j++, currlevel++)
		{
			int si = string[j] - '0';
			if(currlevel>currstanding)
			{	required += currlevel - currstanding;
				currstanding += (currlevel - currstanding);
			}
			currstanding += si;

		}
		cout << "Case #" << i+1 << ": " << required << endl;
	}
	return 0;
}