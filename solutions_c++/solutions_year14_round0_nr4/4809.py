#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	
	for (int i=1;i<=T;++i)
	{
		int N = 0;
		cin >> N;
		
		double a[1000] = {1};
		double b[1000] = {1};
				
		for (int j=0;j<N;++j) 
		{
			cin >> a[j];
		}
		sort(a,a+N);
		
		for (int j=0;j<N;++j)
		{
			cin >> b[j];
		}
		sort(b,b+N);
		
		
		int min_a = 0; 
		int min_b = 0;
		int max_a = N-1; 
		int max_b = N-1;
		
		int scr1 = 0;
		
		for (int j=0;j<N;++j) 
		{
			if (a[min_a] < b[min_b])
			{
				++min_a;
				--max_b;
			}
			
			if (a[min_a] > b[min_b])
			{
				++min_a;
				++min_b;
				++scr1;
			}
		}
		
		
		min_a = 0; 
		min_b = 0;
		max_a = N-1; 
		max_b = N-1;
		int scr2 = 0;
		
		for (int j=0;j<N;++j) 
		{
			if (a[max_a] > b[max_b])
			{
				--max_a;
				++min_b;
				++scr2;
			}
			
			if (a[max_a] < b[max_b])
			{
				--max_a;
				--max_b;
			}
		}
		
		cout <<"Case #"<<i<<": "<<scr1<<" "<<scr2<<endl;
		
	}
}