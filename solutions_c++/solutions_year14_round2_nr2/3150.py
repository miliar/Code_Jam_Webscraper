#include<iostream>

using namespace std;

int dp[1001][1001];

void preProcess()
{
	int i,j;
	for(i =0;i<1001;i++)
	{
		for(j=0;j<1001;j++)
		{
			dp[i][j] = i&j;
		}

	}

}


int main()
{

	preProcess();
	int i,j,a,b,k,cnt;

	int tests,t=0;
	cin>>tests;
	while(t++<tests)
	{
		cin>>a>>b>>k;

		cnt = 0;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if(dp[i][j]<k)
					cnt++;
			}

		}


		cout<<"Case #"<<t<<" "<<cnt<<endl;
	}

	return 0;
}
