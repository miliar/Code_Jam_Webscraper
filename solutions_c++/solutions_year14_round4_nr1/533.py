#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
	static int num[1+700];
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int N,C;
		cin>>N>>C;
		memset(num,0x00,sizeof(num));
		while(--N>=0)
		{
			int s;
			cin>>s;
			num[s]++;
		}
		int A=0;
		for(int i=C;i>=1;i--)
		{
			int j=min(i,C-i);
			while(num[i]!=0)
			{
				num[i]--;
				while(j!=0&&num[j]==0)j--;
				if(j!=0)num[j]--;
				A++;
			}
		}
		cout<<"Case #"<<t<<": "<<A<<endl;
	}
	return 0;
}
