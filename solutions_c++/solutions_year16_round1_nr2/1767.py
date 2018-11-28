#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	
	ifstream infile;
	infile.open("B-large1.in", ios::in);
	
	ofstream outfile;
	outfile.open("B-large1.out", ios::out);

	int T;
	infile>>T;

	int index =1;

	while(T--)
	{
		int N, i,j;
		infile>>N;
		int temp;
		int max = 0;	
		int Aux[2510]={0};

		for(i = 0; i<2*N-1; i++)
		{
			for(j=0; j<N; j++)
			{
				infile>>temp;
				Aux[temp]++;
				
				if(temp >= max)
					max = temp;
			}		
	
		}
		outfile<<"Case #"<<index<<": ";
	
		for(i=1; i<=max; i++)
		{
			if(Aux[i]%2 != 0)
				outfile<<i<<" ";
		}
		outfile<<"\n";
		index++;
	}

	return 0;
}
