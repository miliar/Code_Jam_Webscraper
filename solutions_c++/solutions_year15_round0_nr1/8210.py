#include <iostream>
#include <fstream>

#define MAX_S 1001

using namespace std;

int minCalc(int v[], int smax)
{
	int sum =0;
	int count=0;
	for(int i=0; i < smax; i++)
	{
		sum+=v[i];
		if(sum+count < i+1)
			count++;
	}
	return count;
}
int main()
{
	ifstream in("input.in");
	ofstream out("output.out");

	int T;
	in >> T;
	
	for(int t=0; t < T; t++)
	{
		int smax;
		int v[MAX_S+1];
		in >> smax;
		cout << "S: " << smax << "# ";
		for (int i=0; i < smax+1; i++)
		{
			char c;
			in >> c;
			v[i] = c - '0';
			cout << v[i] << " ";
		}
		cout << endl;
		out << "Case #" << t+1 << ": " << minCalc(v, smax) << endl;
	}
	return 0;
}
