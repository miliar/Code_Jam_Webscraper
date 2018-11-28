#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <unordered_map>

using namespace std;


int main()
{
	freopen("input1.in", "r", stdin);
	freopen("output1.txt","w",stdout);
	ios_base::sync_with_stdio(0);

	int test;
	cin>>test;


	for(int i=1;i<=test;i++)
	{
		int n;
		cin>>n;

		
		long long int num2=n;
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",i);
		}
		else
		{
			unordered_map<char,int> mp;

			long long int index=1,num=0;
			int flag=0;
			while(1)
			{

				num2 = n*index;
				if(num2<0)
				{
					printf("Case #%d: INSOMNIA\n",i);
					flag=1;
					break;
				}
				string temp = to_string(num2);
				for(int j=0;j<temp.size();j++)
				{
					if(mp[ temp[j]  ]==0)
					{
						mp[temp[j] ]=1;
						num++;
					}

				}
				//cout<<num2<<" "<<num<<endl;
				if(num==10)
					break;
				
				index++;
			}
			if(flag==0)
				printf("Case #%d: %lld\n",i,num2);
		}

		

	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}