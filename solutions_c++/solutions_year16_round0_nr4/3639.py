#include <iostream>
using namespace std;

int main()
{
	int TEST_CASES;
	cin>>TEST_CASES;
	int CASE_NUM=0;
	while(TEST_CASES--)
	{
		CASE_NUM++;
		int K,C,S;
		cin>>K>>C>>S;
		if(K!=S)
		{
			cout<<"Case #"<<CASE_NUM<<": "<<"IMPOSSIBLE"<<"\n";
		}
		else
		{
			cout<<"Case #"<<CASE_NUM<<": ";
			for (int i = 0; i < K; ++i)
			{
				cout<<i+1<<" ";
			}
			cout<<"\n";
		}
		
		

	}
	return 0;
}