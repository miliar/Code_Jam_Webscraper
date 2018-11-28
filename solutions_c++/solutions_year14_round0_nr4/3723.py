#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	int num = 0;
	cin >> num;
	int cases = 1;
	while(cases <= num)
	{
		int N;
		int warScore = 0, dWarScore = 0;
		cin>>N;
		double naomi[N], ken[N];
		for(int i = 0; i < N; i ++)
			cin>>naomi[i];
		for(int i = 0; i < N; i ++)
			cin>>ken[i];

		sort(naomi, naomi + N);
		sort(ken, ken + N);
		int i = 0, j = 0;
		while(i < N && j < N)
		{
			if(naomi[i] < ken[j])
			{
				i++;
				j++;
			}
			else
				j++;
		}
		warScore = N - i;

		i = N - 1;
		j = N - 1;
		int naomiStart = 0, kenStart = 0;
		while(i >= naomiStart && j >= 0)
		{
			if(naomi[i] > ken[j])
			{
			 	i--;	
				j--;
				dWarScore ++;
			}
			else
			{
				naomiStart++;
				j--;
			}
		}

		cout<<"Case #"<<cases<<": "<<dWarScore<<" "<<warScore<<endl;
		cases++;
	}
	return 0;
}
