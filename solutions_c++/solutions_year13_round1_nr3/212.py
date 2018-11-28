#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int R, M, N, K;
		cin>>R>>N>>M>>K;
		
		cout<<"Case #"<<caso<<":"<<endl;
		
		for(int i=0; i<R; i++)
		{
			vector <int> p(K);
			for(int j=0; j<K; j++)
				cin>>p[j];
			
			bool done = 0;
			for(int it=0; it<1000; it++)
			{
				int a = 2 + (rand() % (M - 1));
				int b = 2 + (rand() % (M - 1));
				int c = 2 + (rand() % (M - 1));
				
				//cout<<a<<" "<<b<<" "<<c<<endl;
				
				bool ok = 1;
				for(int j=0; j<K; j++)
				{
					if(p[j] == 1 || p[j] == a || p[j] == b || p[j] == c || p[j] == a * b || p[j] == a * c || p[j] == b * c || p[j] == a * b * c);
					else ok = 0;
				}
				
				if(ok)
				{
					cout<<a<<b<<c<<endl;
					done = 1;
					break;
				}
			}
			if(!done) cout<<"222"<<endl;
		}
		
		
	}
	
	return 0;
}
