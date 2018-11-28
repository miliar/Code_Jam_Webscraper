#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	vector<int> members;
	int sum;
	int T, N;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		cin >> N;
		sum = 0;
		for(int j = 0; j < N; j++) 
		{
			int x;
			cin >> x;
			sum += x;
			members.push_back(x);
		}
		cout<<"Case #"<<i<<": ";
		
		int max = 1, poz = 0, liczbaRownychMax = 0, roznica = 0; 
		while( max != 0) 
		{
			max = 0; 
			poz = 0; 
			liczbaRownychMax = 0; 
			roznica = 0;
			for(int j = 0; j < N; j++) 
			{
				if( max == members[j]) {
					liczbaRownychMax++;
				}
				if( max < members[j] ) 
				{
					roznica = members[j] - max;
					max = members[j];
					poz = j;
					liczbaRownychMax = 0;
				}
			}
			if(max > 0) 
			{
				if( liczbaRownychMax == 0) 
				{
					if( roznica >= 1) 
					{
						cout<<(char)('A' + poz)<<" ";
						members[poz] -= 1;
					}
					else {
						cout<<"roznica <= 0?";
					}
				}
				else 
				{
					if( (liczbaRownychMax % 2) == 0) 
					{
						cout<<(char)('A' + poz)<<" ";
						members[poz] -= 1;
					}
					else
					{
						cout<<(char)('A' + poz);
						members[poz] -= 1;
						for(int j = 0; j < N; j++) 
						{
							if( members[j] == max) {
								cout<<(char)('A' + j)<<" ";
								members[j] -=1;
							}
						}
						
					}
				}
			}

		}
		cout<<"\n";
		members.clear();
		
	}
	return 0;
}
