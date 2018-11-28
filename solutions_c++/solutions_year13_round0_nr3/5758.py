#include <iostream>
#include <fstream>

using namespace std;


int palindrom(int broj)
{
	if(broj < 10) return 1;
	int novi=0,t=broj;
	while(t>0)
	{
		novi=(novi*10 + t%10);
		t/=10;
	}

	if(novi == broj)
		return 1;

	return 0;
}

int kvadrat(int broj)
{
	int i = 1;
	while(1)
	{
		if(i*i > broj)
			return 0;

		if(i*i == broj)
		{
			if(palindrom(i))
				return 1;
		}
			

		i++;
	}
}



int main ()
{
	ifstream file("C-small-attempt0.in");

	int broj_primjera,l,d,svi_brojevi;

	file >> broj_primjera;
	

	for(int i = 0;i<broj_primjera;i++)
	{
		svi_brojevi = 0;
		file >> l >> d;

		for(int j = l;j<=d;j++)
		{
			if(kvadrat(j) && palindrom(j))
				svi_brojevi++;
		}

		cout << "Case #" << i+1 <<": " << svi_brojevi << endl;
	}


	file.close();
}