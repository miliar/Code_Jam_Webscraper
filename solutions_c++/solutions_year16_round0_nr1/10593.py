#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	int T;
	bool b;
	int numbers[10] = {0,1,2,3,4,5,6,7,8,9};
	ifstream fin("Counting_Sheep.txt");
	fin >> T;
	long double *N = new long double [T];
	for(int j = 0; j < T; j++)
		fin >> N[j];
	fin.close();
	ofstream fout("Counting.txt");
	for(int j = 0; j < T; j++)
	{
		fout << "Case #" << j+1 << ": ";
		if(N[j] == 0) fout << "INSOMNIA" << endl;
		else 
		{
			int *elem = new int[10];
			int i = 0;
			int l = 0;
			do
			{
				i++;
				int a;
				b = true;
				
				int k = i * N[j];
				for (int p = 199; p >= 0, k != 0; p--)
				{
					a = k%10;
					for(int r=0;r<10;r++)
						if(a == elem[r]) {b=false;break;}
					if(b) {elem[l] = a; l++;b=true;}
					k = (k - k%10)/10;
					b = true;
				}
				
				for(int y=0;y<10;y++)
				{
					b = true;
					for(int s=0;s<10;s++)
						if(elem[y]==numbers[s]) b=false;
					if(b) break;
				}
				
			} while(b!=false);
			fout << setprecision(12) << i * N[j] << endl;
			delete []elem;
		}
	}
	fout.close();

	delete [] N;
	return 0;
}