#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
using namespace std;
void setnumbers(int x , int array[]);
void calc(int x);
int check(int array[]);
void main() {






	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	bool sleep = false;
	int array[10] = { 0,0,0,0,0,0,0,0,0,0 };
	
	
	
	
	
	int n , c , worknumber;
	fin >> n;
	for (int i = 1; i <= n; i++)
	{
		int loop = 1;
		sleep = false;
		fin >> c;
		for (int k = 0; k < 10; k++) { array[k] = 0; }
		if (c == 0) {
			fout << "Case #" << i << ": " <<"INSOMNIA"<<endl;
		}
		else {
			while (!sleep) {
				worknumber = c*loop;
				loop++;
				setnumbers(worknumber, array);
				if (check(array))
				{
					fout << "Case #" << i << ": " << worknumber << endl;
					sleep = true;
				}
			}

		}

	}


	
	cin.get();
}
void setnumbers(int x , int array[]) {
	while (x)
	{
		int a = x % 10;
		x = x / 10;
		array[a] = 1;
	}
}

int check(int array[])
{
	int x = 1;
	for (int i = 0; i < 10; i++) {
		x *= array[i];
	}
	return x;
}

