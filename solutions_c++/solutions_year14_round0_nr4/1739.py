#include<iostream>
#include<fstream>
#include<algorithm>

using namespace std;

int war(float* naomi, float* ken, int size)
{
	int naomiwin = 0;

	int naomia = 0, naomib = 0, kena = 0, kenb = 0;

	for (int i = 0; i < size; i++)
	{
		
		if (naomi[size - naomib] > ken[size - kenb])
		{
			naomiwin++;
			naomib++;
			kena++;
		}
		else
		{
			naomib++;
			kenb++;
		}

	}
	return naomiwin;
}

int dwar(float* naomi, float* ken, int size)
{
	int naomiwin = 0;

	int naomia = 0, naomib = 0, kena = 0, kenb = 0;

	for (int i = 0; i < size; i++)
	{
		if (naomi[1 + naomia] < ken[1 + kena])
		{
			naomia++;
			kenb++;
		}
		else
		{
			naomiwin++;
			naomia++;
			kena++;
		}
	}
	return naomiwin;
}


int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");


	int T = 0;
	in >> T;
	for (int i = 1; i <= T; i++)
	{
		int size = 0;
		in >> size;
		float naomi[1005], ken[1005];
		
		//init
		for (int j = 0; j < 1005; j++)
		{
			naomi[j] = 0;
			ken[j] = 0;
		}
		//get input
		for (int j = 1; j <= size; j++)
		{
			in >> naomi[j];
		}
		for (int j = 1; j <= size; j++)
		{
			in >> ken[j];
		}
		sort(naomi + 1, naomi + 1 + size);
		sort(ken + 1, ken + 1 + size);
		
		out << "Case #" << i << ": " <<dwar(naomi, ken, size) << " " << war(naomi, ken, size) << endl;

	}


	in.close();
	out.close();

	return 0;
}