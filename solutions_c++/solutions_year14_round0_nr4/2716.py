#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

double w1[1005];
double w2[1005];

int main()
{
	ios_base::sync_with_stdio(0);
	int testy, n, wyn1, wyn2, poz;
	
	cin >> testy;
	for(int j=1; j<=testy; j++)
	{
		cin >> n;
		for(int i=1; i<=n; i++)
		{
			cin >> w1[i];
		}
		for(int i=1; i<=n; i++)
		{
			cin >> w2[i];
		}
		
		sort(w1+1, w1+n+1);
		sort(w2+1, w2+n+1);
		
			
		
		wyn1=n;
		wyn2=0;
		
		poz=1;
		for(int i=1; i<=n; i++)
		{
			while(w2[poz]<w1[i] && poz<=n) poz++;
			if(poz>n) break;
			else
			{
				wyn1--;
				poz++;
			} 
		}
		
		poz=1;
		for(int i=1; i<=n; i++)
		{
			if(w2[poz]<w1[i]) {wyn2++; poz++;}
			
		}
				
		cout << "Case #" << j << ": " << wyn2 << " " << wyn1 << endl;
	}
	
	cin.ignore();
	getchar();
	return 0;
}



