#include <iostream>

using namespace std;

int main()
{
	int senator_count[26];
	char parties[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	int T; cin>>T;

	for(int i = 1; i <= T; i++)
	{
		int N; cin>>N;
		int total = 0;
		for(int j = 0; j < N; j++)
		{
			cin>>senator_count[j];
			total += senator_count[j];
		}

		cout<<"Case #"<<i<<": ";

		while (total > 0)
		{
			int first, second;
			if(total > 3)
			{
				// Find the party with most senators left
				int largest = 0;
				for(int j = 1; j < N; j++)
				{
					if(senator_count[j] > senator_count[largest])
						largest = j;
				}
				senator_count[largest]--;
				cout<<parties[largest];
				total--;

				// Find the party with most senators left now (second evac)
				largest = 0;
				for(int j = 1; j < N; j++)
				{
					if(senator_count[j] > senator_count[largest])
						largest = j;
				}
				senator_count[largest]--;
				cout<<parties[largest]<<" ";
				total--;
			}
			else
			{
				if(total == 3)
				{
					int largest = 0;
					for(int j = 1; j < N; j++)
					{
						if(senator_count[j] > senator_count[largest])
							largest = j;
					}
					senator_count[largest]--;
					cout<<parties[largest]<<" ";

					for(int j = 0; j < N; j++)
					{
						if(senator_count[j] > 0)
							cout<<parties[j];
					}

					total-=3;
				}
				else if(total == 2)
				{
					for(int j = 0; j < N; j++)
					{
						if(senator_count[j] > 0)
							cout<<parties[j];
					}
					total-=2;
				}
				cout<<endl;
			}
		}
	}
}