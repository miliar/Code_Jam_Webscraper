#include<iostream>
using namespace std;
int main()
{
	int tt,s_max;

	cin>>tt;
	cin.ignore();
	for(int i=1 ; i<=tt ; i++ )
	{
		int sum=0;
		int ans=0,yy=0;

		char aud[7]; //for audience
		char inp[10]; //for input

		cin.getline(inp,10);
		s_max=inp[0] - 48;
		int in=2;
		while(yy<=s_max)//storing the no of audiences
		{
			aud[yy]=int(inp[in]);
			yy++;
			in++;
		}
		for(int j=0 ; j<=s_max ; j++)
		{
			sum = sum + (aud[j]-48);
			if((sum+ans)<(j+1))
				++ans;
			else
				continue;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;

	}
}
