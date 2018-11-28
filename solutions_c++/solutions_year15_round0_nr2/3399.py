#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	int i;
	for(i=0; i<t; i++)
	{
		int d; 
		scanf("%d", &d);
		int maximum = -1;
		std::vector<int> pancakes;
		for(int j = 0; j<d; j++)
		{
			int p;
			scanf("%d",&p);
			if(maximum < p)
				maximum = p;
			pancakes.push_back(p);
		}
		int minimum = 999999;
		for(int k = 1; k<=maximum; k++)
		{ 
			int timetaken = 0;
			for(int l = 0; l < d ; l++)
			{
				if(ceil(pancakes[l] * 1.0/k) > 0)
					timetaken += (ceil(pancakes[l] * 1.0/k) - 1);

			}
			timetaken += k;
			if(minimum > timetaken)
				minimum = timetaken;



		}	
		cout << "Case #" << i+1 << ": " << minimum << endl;
	}
	return 0;
}