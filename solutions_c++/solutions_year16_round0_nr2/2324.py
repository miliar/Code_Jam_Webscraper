#include <iostream>
#include <cstdio>
#include <string>


using namespace std;



int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output1.txt","w",stdout);
	ios_base::sync_with_stdio(0);

	int test;
	cin>>test;

	for(int t=1;t<=test;t++)
	{
		string s;
		cin>>s;

		int ans=0;

		
		for(int i=1;i<s.size();i++)
		{
			if(s[i]!=s[i-1])
			{
				ans++;
			}
		}

		if(s[ s.size()-1 ]=='-')
		{
			ans++;
		}


		printf("Case #%d: %d\n",t,ans);



	}
	fclose(stdin);
	fclose(stdout);	
	return 0;
}