//============================================================================
// Name        : Counting.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream input ;ofstream output;
	input.open("input");
	output.open("output");
	const int source[]={0,1,2,3,4,5,6,7,8,9};

	int t,k=0;
	//bool done =false;
	input>>t;
	while(k++!=t)
	{
		int data[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
		unsigned long long int n;
		input>>n;

		if(n==0)
		{output<<"Case #"<<k<<": INSOMNIA"<<endl;cout<<"Case #"<<k<<": INSOMNIA"<<endl;}
		else
		{
			for(int i =1;;i++)
			{
				unsigned long long int G = (i*n);
				while(G!=0)
				{
					int tmp = G%10;
					data[tmp]=tmp;
					G/=10;
					//cout<<tmp<<endl;
				}
				if(source[0]==data[0] && source[1]==data[1] && source[2]==data[2] && source[3]==data[3] && source[4]==data[4] && source[5]==data[5] && source[6]==data[6] && source[7]==data[7] && source[8]==data[8] && source[9]==data[9])
				{
					output<<"Case #"<<k<<": "<<(unsigned long long int)(i*n)<<endl;
					cout<<"Case #"<<k<<": "<<(unsigned long long int)(i*n)<<endl;
					break;
				}

			}
		}
	}
	input.close();
	output.close();
	return 0;
}
