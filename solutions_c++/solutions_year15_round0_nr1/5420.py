#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,smax;
	int no=0;
	cin>>t;
	while(t--)
	{
		char s[1001]={'\0'};
		cin>>smax;
		cin>>s;
		
		no++;
		int sum = s[0]-'0';
		int k,count=0;
		for(int i=1;i<strlen(s);i++)
		{
			k = s[i]-'0';
			if(k > 0)
			{
				if(sum < i)
				{
					count += (i-sum);
					sum += count;
				}
				sum += k;
			}
		}
		cout<<"Case #"<<no<<": "<<count<<endl;
	}
}
