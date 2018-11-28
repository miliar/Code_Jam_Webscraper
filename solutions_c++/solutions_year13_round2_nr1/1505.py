#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	long long N;
	cin>>N;
	for (long long i = 0; i < N; ++i)
	{
		long long A,S;
		cin>>A>>S;
		long long B=A;
		long long M[S];
		for (long long j = 0; j < S; ++j)
		{
			cin>>M[j];
		}
		sort(M,M+S);
		long long count=0;
		long long count1=0;
		if(A==1)count=S;
		else
		{
			for (long long j = 0; j <S ; ++j)
			{
				if(M[j]<A)
				{
					A+=M[j];
					continue;
				}
				if(j==S-1)
				{
					if(M[j]>=A)count++;
					break;
				}
				if(M[j]>=A)
				{
					while(A<=M[j])
					{
						A+=(A-1);
						count++;
					}
					A+=M[j];
					continue;
				}
				else
				{
					count++;
				}
			}
		}
		if(count>=S)
		{
			for (long long j = 0; j < S; ++j)
			{
				if(M[j]<B)
				{
					B+=M[j];
					count1++;
				}	
			}
			count=S-count1;
		}
		cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	return 0;
}