#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

int main() 
{ _
	int t;
	cin>>t;
	int temp = t;
	while(t--)
	{
		int sn;cin>>sn;
		string a;cin>>a;
		int shy[sn+1];
		for (int i = 0; i < sn+1; ++i)
		{
			shy[i] = a[i] - '0';
		}
		int no=0;
		int add = 0;
		int addcount = 0;
		for (int i = 0; i < sn+1; ++i)
		{
			if(shy[i] > 0)
				no = no + shy[i];
			else if(shy[i] == 0 && no > i)
			{

			}
			else if(shy[i] == 0 && no <= i)
			{
				add = i - no + 1;
				no = no + add;
				addcount += add;
				add = 0;
			}
		}
		cout<<"Case #"<<temp-t<<": "<<addcount<<endl;
	}
	return 0;
}
