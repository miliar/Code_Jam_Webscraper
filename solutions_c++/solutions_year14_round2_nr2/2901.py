#include <iostream>
#include <fstream>
using namespace std;
long int A , B , K;
long int total , count;
int main()
{

	ifstream ifile;
	ofstream ofile;
	ofile.open("output.txt");
	ifile.open("B-small-attempt0.in");

	ifile>>total;



	for(long int l=0;l<total; l++)
	{
		ifile>>A>>B>>K;
	count =0;
	for(long int i= 0  ;i<A; i++)
	{
	for(long int j=0  ;j<B; j++)
	{
		if((j&i)<K)
			count++;

	}


	}
	ofile<<"Case #"<<l+1<<": "<<count<<endl;
	}
	
	return 0;
}
