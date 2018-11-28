#include<fstream>
using namespace std;

main()
{
	fstream in("input.in");
	fstream out("output.out");
	
	int t,Smax,sum,ans,A[1024],temp;
	char S[1024];
	
	in>>t;
	for(int x=1;x<=t;x++)
	{
		in>>Smax;
		for(int i=0;i<=Smax;i++)
		 A[i]=0;
		for(int i=0;i<=Smax;i++)
		{
			in>>S[i];
			A[i]=S[i]-48;
		}
		sum = A[0];
		ans = 0;
		for(int i=1;i<=Smax;i++)
		{
			if(sum>=i)
			{
				sum+=A[i];
				continue;
			} 
			else
			{
				temp = i-sum;
				ans += temp;
				sum += A[i]+temp;
			}
		}
		out<<"Case #"<<x<<": "<<ans<<"\n"; 
	}
}
