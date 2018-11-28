#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	fstream plik;
	plik.open("wyjscie.txt", ios::in | ios::out);
	int t; cin>>t;
	for(int k=1; k<=t; k++)
	{
		int a, b, x;
		vector <int> n, m;
		cin>>a;
		for(int i=1; i<=4; i++)
		for(int j=1; j<=4; j++)
		{
			cin>>x;
			if(i==a) n.push_back(x);
		}
		cin>>b;
		for(int i=1; i<=4; i++)
		for(int j=1; j<=4; j++)
		{
			cin>>x;
			if(i==b) m.push_back(x);
		}
		int licznik=0;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++) if(n[i]==m[j]) {licznik++; x=n[i];}
		switch(licznik)
		{
			case 0:
				plik<<"Case #"<<k<<": Volunteer cheated!\n";
				break;
			case 1:
				plik<<"Case #"<<k<<": "<<x<<"\n";
				break;
			default:
				plik<<"Case #"<<k<<": Bad magician!\n";
				break;
		}
	}
	plik.close();
	return 0;
}

