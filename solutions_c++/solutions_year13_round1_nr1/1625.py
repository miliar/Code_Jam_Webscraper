#include <iostream>
#include <fstream>

//#define PI 3.1415926

using namespace std;

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	

//	FILE * input;
//	input = fopen("input.txt","r");

	int T;

//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input>>T;// cout<<n<<endl;
	
	/*long long*/ int r,t,n;


	for(int i=0;i<T;i++)
	{

		input>>r>>t;
		n=(-(2*r-1)+sqrt((2*r-1)*(2*r-1)+8*t))/4;
//		cout<<n<<endl;
		output<<"Case #"<<i+1<<": "<<n<<endl;
	}
		
	input.close();
	output.close();
//	system("pause");
	return 0;
}
