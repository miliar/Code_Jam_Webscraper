#include<iostream>
#include<iomanip>
#include<math.h>
#include<string>
#include<stdlib.h>
#include<algorithm>
using namespace std;


int main()
{

	int T,N[103],m[103][1002];
	cin>>T;
	long meth1[103],meth2[103];
	for(int i=1; i<=T; i++)
	{
		cin>>N[i];
		for(int j = 0; j<N[i];j++)
			cin>>m[i][j];
	}
	for(int i=1; i<=T; i++)
	{
		meth1[i] = 0;
		meth2[i] = 0;
		int rate = 0;
		for(int j=0;j<N[i]-1;j++)
		{
			if(m[i][j]>m[i][j+1])
			{
				meth1[i]+=m[i][j]-m[i][j+1];
				if((m[i][j]-m[i][j+1])>rate)
					rate = m[i][j]-m[i][j+1];
			}
		}		
		for(int j=0;j<N[i]-1;j++)
		{
			if(m[i][j]<=rate)
			{
				meth2[i]+=m[i][j];
			}
			else
			{
				meth2[i]+=rate;
			}
		}

	}
	for (int i = 1; i <= T; i++)
	{
		cout<<"Case #"<<(i)<<": "<<meth1[i]<<" "<<meth2[i]<<"\n";
	}
	return 0;
}
