#include <iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	int tot[T];
	for (int l = 0; l < T; ++l)
	{
		int Smax;
		cin>>Smax;
		int Number,S[Smax+1];
		cin>>Number;
		for (int j = 0; j <=Smax ; ++j)
		{
			S[Smax-j]=(Number%10);
			Number=Number/10;
		}
		int total=0,sum=S[0];
		for (int i = 1; i <=Smax; ++i)
		{
			if (i<=sum)
				{
					sum+=S[i];	
					continue;}
			total+=(i-sum);
			sum=S[i]+i;
		}
		tot[l]=total;
		/*for (int i = 0; i <=Smax; ++i)
		{
			cout<<i<<" "<<S[i]<< endl;
		}*/
	}
	for (int i = 0; i < T; ++i)
	{
		cout<< "Case #"<<i+1<<": "<<tot[i]<<endl;
	}
	return 0;
}