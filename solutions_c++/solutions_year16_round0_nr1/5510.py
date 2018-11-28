#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);

	for(int s=0; s<t; s++)
	{
		string check = "0000000000";
		string num;
		cin >> num;
		string res=num;

		if(num=="0")
		{
			printf("Case #%d: INSOMNIA\n",s+1);
		}
		else
		{
			for(int i=0; i<num.size();i++)
			{
				int r = num[i]-48;
				check[r]='1';
			}
			int m = 2;
			while(check != "1111111111")
			{
				int temp = stoi(num)*m;
				res = to_string(temp);
				for(int i=0; i<res.size();i++)
				{
					int r = res[i]-48;
					check[r]='1';
				}
				++m;
			}

			cout<<"Case #"<< s+1 << ":"<< " " << res <<"\n";
		}
	}

	return 0;
}