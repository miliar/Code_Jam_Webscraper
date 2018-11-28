#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int i,j,k,n;
	int num[5]={1,4,9,121,484};
	int A,B;
	ifstream in;
	ofstream out;
	in.open("C-small-attempt0.in");
	out.open("outout.in");
	in >> n;
	string line;
	getline(in, line);
	for(k=0;k<n;k++)
	{
		j=0;
		in >> A;
		in >> B;
		for(i=0;i<5;i++)
			if(A<=num[i] && num[i]<=B)
				j++;
		out << "Case #" << k+1 << ": " << j << "\n";
	}
	in.close();
	out.close();
	return 0;
}