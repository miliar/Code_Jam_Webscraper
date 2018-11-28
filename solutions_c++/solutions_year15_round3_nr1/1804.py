#include<fstream>
#include<iostream>
#include <iomanip>

using namespace std;

int main()
{	

	ifstream input;
 	ofstream output;
 	input.open("cj1a.txt");
 	output.open("answer.txt");
	int n,t,r,c,w,z;
	input>>t;
	int ss=t;
	while(t--){
		input>>r>>c>>w;
		z=(c)/w+(w-1);
		if((c%w)!=0)
			z++;
		z*=r;
		output<<"Case #"<<ss-t<<": "<<z<<endl;
	}
	return 0;
}
