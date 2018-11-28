#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream in;
	in.open("A-small-attempt7.in");
	ofstream out;
	out.open("ssa.out");
	int n, w, z;
	int *a;
	string anas;
	in >> n;
	for (int j = 1; j <= n;j++)
	{
		in >> w;
		in >> anas;
		z = 0;//it counts how many people is less than this iTH
		int k = 0;
		for (int i = 0; i <=w; i++)
		{
			if (i <= z || anas[i]=='0')
				z +=anas[i] - 48;
			else{
				k += i - z;
				z += k+anas[i]-48;
			}
		}
	
		out << "Case #" << j << ": " << k << endl;
	}

	return 0;
}