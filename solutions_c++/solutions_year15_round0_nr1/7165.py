#include "bits/stdc++.h"
using namespace std;

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio();

	int t;
	cin>>t;
	for (int case_no = 1; case_no <= t; ++case_no)
	{
		int n;
		cin>>n;

		string s;
		cin>>s;

		int current_sum=0;
		int people_req=0;
		for (int i = 0; i < s.length(); ++i)
		{
			if ((s[i]-'0')>0)
			{
				if (current_sum<i)
				{
					people_req += i - current_sum;
					current_sum +=(i- current_sum);
				}
				current_sum += (s[i]-'0');
			}
		}

		cout<<"Case #"<<case_no<<": "<<people_req<<"\n";
	}
	return 0;
}