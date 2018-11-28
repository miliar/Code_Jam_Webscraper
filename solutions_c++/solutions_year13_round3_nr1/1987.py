
#include <iostream>
#include <cstdio>
#include <cstring>
#include <stdio.h>

using namespace std;

string str;

char aa[5]={'a','e','i','o','u'};
int str_num[1000002];
int main()
{
	int t,n;
	cin>>t;
	int ca=0;
	while(t--)
	{
		ca++;
		cin>>str>>n;
		int l=str.size();
		memset(str_num,0,sizeof(str_num));
		for (int i=1;i<=l;i++)
		{
			bool is_ok=0;
			str_num[i]=str_num[i-1];
			for (int j=0;j<5;j++)
				if (str[i-1]==aa[j])
				{
					is_ok=1;
					break;
				}
			if (!is_ok)
				str_num[i]++;
			else 
				str_num[i]=0;
//			cout<<str_num[i]<<endl;
		}
		long long res=0;
		for (int i=0;i<l;i++)
		{
			int index=i;
			int end=-1;
			for (int j=i+n-1;j<l;j++)
			{
				int index2=j+1;
				if (str_num[index2]>=n)
				{
					end=j;
					break;
				}
			}
			if (end<0)
				break;
			res+=(l-end);
		}
		cout<<"Case #"<<ca<<": "<<res<<endl;
	}
}

