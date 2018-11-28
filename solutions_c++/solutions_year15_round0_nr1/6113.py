#include <iostream>
using namespace std;
#include <fstream>

void shyness(int HS)
{





}


int * ctoi(char * a, int HS)
{
	int * arr = new int[HS];

	for (int i = 0; i < HS; i++)
	{
		arr[i] = a[i] - '0';
	}
	return arr;
}

int sum = 0;
int main()
{
	fstream file;
	
	file.open("A-large(1).in");
	fstream fout;

	fout.open("output.txt" , ios::out);


		int num;
		file >> num;

		int HS = 0;
		


		for (int k = 1; k < num + 1; k++)
		{

			file >> HS;
			HS++;

			char * a = new char[HS];
			file >> a;

			int * arr = ctoi(a, HS);

			int standing = 0;
			int dost = 0;

			for (int i = 0; i < HS; i++)
			{
				while (standing < i)
				{
					standing++;
					dost++;
				}
				if (standing >= i)
				{
					standing += arr[i];
				}

			}

			fout << "Case #" << k<<": " << dost<<endl;
		}


}
			/*
			int standing = 0;

			int dost=0;
			while (1){
				for (int i=0; standing >= i; standing = arr[i] + standing, i++)
				{
					if (HS == i)
						break;

				}
				if (standing > HS)
					break;
				dost++;
				standing = dost;

			}
			sum = 0;
			if (dost == 0)
			{
				cout << "Case"<<count <<":"<< 0<<endl ;
			}
			else {


			}
			count++;
			*/