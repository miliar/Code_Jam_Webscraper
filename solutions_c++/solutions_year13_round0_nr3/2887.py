#include <iostream>
#include <math.h>
using namespace std;


bool isPalin(long long v)
{
	int bit[15];
	int i=0;
	while(v>0)
	{
		bit[i]=v%10;
		v=v/10;
		i++;
	}
	for(int j=0;j<i/2;j++)
	{
		if(bit[j]!=bit[i-j-1])
			return false;
	}
	return true;
}

int main()
{	
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	int testcase;
	int ans=0;
	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		ans=0;
		long long A,B;
		cin>>A>>B;
		long long i=(long long)(sqrt(A*1.0));
		for (;;i++) 
		{	
			long long v=i*i;
			if(v>B)
				break;
			if(v<A)
				continue;
			if(isPalin(i)&&isPalin(v))
					ans++;
			
		}
		cout<<ans;
		printf("\n");
	}

	return 0;
}

