#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{

	freopen("D-small-attempt1.in","r",stdin);
	freopen("out.in","w",stdout);
	int t,count=0;
	cin>>t;
	double d;
	while(t--)
	{
		count++;
		int s,c1=0,c2;
		cin>>s;
		vector<double>v1;
		vector<double>v2;

		for(int i=0;i<s;i++)
		{
			cin>>d;
			v1.push_back(d);

		}

		for(int i=0;i<s;i++)
		{
			cin>>d;
			v2.push_back(d);

		}

		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());

		vector<double>x1;
		vector<double>x2;
		x1=v1;
		x2=v2;

		c1=0;
		for(int w=v2.size()-1;w>=0;w--)
		{
			
			for(int i=v1.size()-1;i>=0;i--)
				if(v1[w]>v2[i])
				{c1++;v2[i]=3;break;}

				
		}

		c2=v1.size();
		
		
		for(int w=x2.size()-1;w>=0;w--)
		{
			
			for(int i=x1.size()-1;i>=0;i--)
				if(x2[w]>x1[i])
				{c2--;x1[i]=3;break;}

				
		}

		printf("Case #%d: %d %d\n",count,c1,c2);
	}


}



