#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int i = 0; i < T; ++i)
	{
		int N,M;
		cin>>N>>M;
		int Lawn[N][M];
		for (int j = 0; j < N ; ++j)
		{
			for (int k = 0; k < M; ++k)
			{
				cin>>Lawn[j][k];
			}
		}
		int Flag=0;
		for (int j = 0; j < N ; ++j)
		{
			for (int k = 0; k < M; ++k)
			{
				int count=0;
				if(*max_element(Lawn[j],Lawn[j]+M)>Lawn[j][k])
					++count;
				for (int l = 0; l < N; ++l)
				{
					if(Lawn[l][k]>Lawn[j][k])
					{
						++count;
						break;
					}
				}	
				if(count==2)
				{
					Flag=1;
					break;
				}	
			}
			if(Flag==1)break;
		}
		if(Flag==0)
			cout<<"Case #"<<i+1<<": YES\n";
		else
			cout<<"Case #"<<i+1<<": NO\n";
	}
	return 0;
}