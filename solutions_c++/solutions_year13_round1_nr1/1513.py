#include <iostream>
#include <fstream>
using namespace std;
#define pi 3.14;

int main()
{
    ifstream infile("A-small-attempt0.in");
	ofstream outfile("outfile.out");
	int N;
	infile>>N;
	for(int i=0;i<N;i++)
	{
		long long r,t;
		infile>>r>>t;
        int k=0;
		while(1)
		{
			r++;
			t-=(r*r-(r-1)*(r-1));
			if(t<0) break;
			r++;
			k++;
		}
		outfile<<"Case #"<<i+1<<": "<<k<<endl;
	}
	infile.close();
	outfile.close();
}