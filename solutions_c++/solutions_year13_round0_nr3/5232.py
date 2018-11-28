#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int A, T,  C, D;
	 ifstream fin;
	 ofstream fout;
	 fin.open("C-small-attempt1.in");
	 fout.open("lol.txt");
	fin >> A;
	fin.get();
	for(int i = 0; i < A; i++)
	{
		fin >> T;
		fin.get();
		fin >> D;
		fin.get();
		int B = 1;
		 
		 
		 
		if(D >= 4)
			B++;
		if(D >= 9)
		   B++;
		if(D >= 121)
			B++;
		if(D >= 484)
			B++;
		if(T > 1)
			B--;
		if(T > 4)
			B--;
		if(T > 9)
			B--;
		if(T > 121)
			B--;
		if(T > 484)
			B--;
		C = B;
		fout << "Case #" << i+1 << ": " << C << endl;
	}
	cout << "lol";
	while(true);
	return 0;
}

