#include <bits/stdc++.h>

using namespace std;

int main()
{
	unsigned long long T, N, aux, last;
	
	cin >> T;
	
	for(int t = 1; t <= T; t++)
	{
		cin >> N;
		
		if(!N)
			cout << "Case #" << t << ": INSOMNIA\n";
		else
		{
			set<unsigned long long> mset;
			
			for(int i = 0; i < 10; i++)
				mset.insert(i);
			
			for(int i = 1; !mset.empty(); i++)
			{	
				last = aux = N*i;
				
				while(aux > 0)
				{
					if(mset.find(aux%10) != mset.end())
						mset.erase(aux%10);
					
					aux /= 10;
				}
			}
			
			cout << "Case #" << t << ": " << last << endl; 
		}
	}
	return 0;
}
