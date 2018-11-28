#include<cstdio>
#include<iostream>
using namespace std;

int line1[20];
int line2[20];

int main()
{
	ios_base::sync_with_stdio(0);
	int testy, a, b, x, liczba, acht;
	cin >> testy;
	for(int j=1; j<=testy; j++)
	{
		cin >> a;
		for(int i=1; i<=4; i++)
		{
			for(int r=1; r<=4; r++)
			{
				cin >> x;
				line1[x]=i;
			}
		}
		cin >> b;
		for(int i=1; i<=4; i++)
		{
			for(int r=1; r<=4; r++)
			{
				cin >> x;
				line2[x]=i;
			}
		}
		liczba=(-1); acht=0;
		for(int i=1; i<=16; i++)
		{
			if(line1[i]==a && line2[i]==b && liczba==(-1)) liczba=i;
			else if(line1[i]==a && line2[i]==b && liczba>0) acht=5;
		}
		cout << "Case #" << j << ": ";
		if(acht==5) cout << "Bad magician!";
		else if(liczba==(-1)) cout << "Volunteer cheated!";
		else cout << liczba;
		
		cout << endl;
	}
	
	cin.ignore();
	getchar();
	return 0;
}



