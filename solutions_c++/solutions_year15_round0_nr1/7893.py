#include <iostream>
#include <fstream>
using namespace std;

int main(){

	ifstream mf;
	ofstream out;
	out.open("output.txt");
	mf.open("input.txt");
	int k;
	mf >> k;

	for (int i = 1; i <= k; i++)
	{
		int shy[1001];
		int num;
		char c;
		mf >> num;
		int j;
		for (j = 0; j <= num; j++)
		{
			mf >> c;
			shy[j] = c - '0';
		}

		int sum = 0;
		int temp;
		for (int u = 0; u < j; u++)
		{
			/*if (u > sum)
				out << "Case #" << i << ": " << u-sum << endl;
			else
				out << "Case #" << i << ": " << 0 << endl;
			*/
			temp = shy[u];
			shy[u] = u-sum;
			sum += temp;
		}
		int max = 0;
		for (int u = 0; u < j; u++)
		{
			if (shy[u]>max)
				max = shy[u];
		}
		out << "Case #" << i << ": " << max<<endl;
	}
	out.close();
	mf.close();
	return 1;
}