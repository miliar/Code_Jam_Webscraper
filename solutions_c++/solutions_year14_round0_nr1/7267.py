#include <iostream>
#include <cstdio>
using namespace std;
int tab1[5];
int tab2[5];
int a;
int c;
int q;
int wynik;
int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 0 ; i < n ; i++)
	{
		scanf("%d", &a);
		for(int j = 0 ; j < (a-1) * 4 ; j++)
		{
			scanf("%d", &c);
		}
		for(int j = 0 ; j < 4 ; j++)
		{
			scanf("%d", &tab1[j]);
		}
		for(int j = 0 ; j < ((4-a) * 4) ; j++)
		{
			scanf("%d", &c);
		}
//////////////////////////////////////////////////		
		scanf("%d", &a);
		for(int j = 0 ; j < (a-1) * 4 ; j++)
		{
			scanf("%d", &c);
		}
		for(int j = 0 ; j < 4 ; j++)
		{
			scanf("%d", &tab2[j]);
		}
		for(int j = 0 ; j < ((4-a) * 4) ; j++)
		{
			scanf("%d", &c);
		}
//////////////////////////////////////////////////
		wynik=0;
		for(int x = 0 ; x < 4 ; x++)
		{
			for(int y = 0 ; y < 4 ; y++)
			{
				if(tab1[x]==tab2[y])
				{
					wynik++;
					//cout<<x<<" "<<y<<endl;
					q=tab1[x];
				}
			}
		}
		//cout<<"-->"<<wynik<<endl;
		if(wynik==0)
		{
			cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		}
		if(wynik==1)
		{
			cout<<"Case #"<<i+1<<": "<<q<<"\n";
		}
		if(wynik>1)
		{
			cout<<"Case #"<<i+1<<": Bad magician!\n";
		}
	}
	
	return 0;
}