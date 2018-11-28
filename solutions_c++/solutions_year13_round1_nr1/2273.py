#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	ifstream input("E:\\input1.txt");
	ofstream output("E:\\output.txt");
	

	int total;
	input>>total;

	for(int i=0; i<total; i++)
	{
		__int64 r,t,x;
		input>>r;
		input>>t;
		

		__int64 a= -2, b = 1-2*r, c=t;
		x = (-b-sqrt(b*b-4*a*c))/(2*a);

		output<<"Case #"<<i+1<<": "<<x<<endl; 
		cout<<"Case #"<<i+1<<": "<<x<<endl; 
		
	}
	


	//cout<<"Hello"<<endl;
	return 0;
}