#include <fstream>
#include <algorithm> 
using namespace std;

int main()
{
	ifstream fin("C://Users/dmx/Desktop/D-large.in");
	ofstream fout("C://Users/dmx/Desktop/answer4-large.txt");
	int t, i, n, j, k, y, z;
	fin>>t;
	double Naomi[1010], Ken[1010];
	for(i = 0; i < t; i++)
	{
		y = z = 0;
		fin>>n;
		for(j = 0; j < n; j++)
		{
			fin>>Naomi[j];
		}
		for(j = 0; j < n; j++)
		{
			fin>>Ken[j];
		}
		sort( Naomi, Naomi + n );
		sort( Ken, Ken + n );
		j = k = 0;
		while(k < n)
		{
			if( Ken[k] > Naomi[j] )
			{
				j++;
				k++;
				y++;
			}
			else
				k++;
		}
		j = k = 0;
		while(j < n)
		{
			if( Naomi[j] > Ken[k] )
			{
				j++;
				k++;
				z++;
			}
			else
				j++;
		}
		fout<<"Case #"<<i+1<<": "<<z<<' '<<n-y<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}