#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
using namespace std;

int tc=0,s;
string inp;
int main()
{
	cin >> tc;
	for( int k =1 ; k<= tc ; k++ )
	{
		cin >> s >> inp;
		int ccp = 0;
		int res = 0;
		for(int i=0;i<s+1;i++)
		{
			int req_people	= inp[i] - '0';
			res		= res + max(0,(req_people==0?0:i) - ccp);
			ccp		= ccp + req_people + max(0,(req_people==0?0:i)-ccp);
			//cout << i << " " << res << endl; 
		}
		cout << "Case #" << k << ": " << res << endl;
	}
	return 0;
}
