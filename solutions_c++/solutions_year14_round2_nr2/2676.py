#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#define REP(I,N) for(int I = 0; I < N; ++I)
#define REPN(I,N) for(int I = 1; I <= N; ++I)
using namespace std;
typedef vector<int> VI;

int main()
{
	int ileTestow, a, b, k, z, wynik = 0;
	
	scanf("%d", &ileTestow);
	REPN(i, ileTestow)
	{
		scanf("%d %d %d", &a, &b, &k);
		REP(x, a)
		{
			REP(y, b)
			{
				//cout<<"x = "<<x<<", y = "<<y<<endl;
				z = x & y;
				if(z < k)  
				{
					//cout<<(x & y)<<endl;
					++wynik;
				}
			}
		}
		
		
		printf("Case #%d: %d\n", i, wynik);
		
		wynik = 0;
	}
}
