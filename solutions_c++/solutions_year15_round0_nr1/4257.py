#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int M;
		cin>>M;
		char shy[1010];
		cin>>shy;
		int len=strlen(shy);
		int need=0,standing=shy[0]-'0';
		for(int j=1;j<len;j++)
		if(shy[j]!='0')
		{
			if(standing<j)
				{
					int x=j-standing;
					need+=x;
					standing+=x;

				}
			standing+=shy[j]-'0';
		}
		cout<<"Case #"<<i+1<<": "<<need<<endl;

	}
	return 0;
}