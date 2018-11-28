#include<iostream>
using namespace std;
#include<fstream>

int main()
{
	ifstream in("B-small-attempt0.in");
	ofstream out("output.txt");
	
	double t, a , b, k, count;
	in>>t;
	for(int i =1 ; i<=t ; i++)
	{
		count=0;
		in>>a;
		in>>b;
		in>>k;
		for(int j = 0 ; j<a; j++)
		{
			for(int l = 0; l<b; l++)
			{
				//cout<<(j&l)<<endl;
				if((j&l)<k)
				count++;
			}
		}
		out<<"Case #"<<i<<": "<<count<<endl;
	}
	
	return 0 ;
}
