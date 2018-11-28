#include <iostream>
#include <fstream>
using namespace std;

main()
{
	int i,j,k;
	int T;
	int y;
	double t,r;
	double sum; 
	ifstream infile("input");
	ofstream outfile("output",ios_base::app);
	infile>>T;
	for(i=0;i<T;i++)
	{	
		sum=0;
		y=0;
	//	while(1)
	//	{
			infile>>r;
//cout<<r<<endl;

			infile>>t;
//cout<<t<<endl;
			for(j=1;j<4000;j++)
			{
//cout<<j<<endl;
//cout<<sum<<endl;
//cout<<t<<endl;
				if(sum>t)
				{
					y=j/2-1;
					break;
				}
				if(sum==t)
				{
					y=j/2;
					break;
				}
				if((j%2)==1)
				{
				sum=(r+j)*(r+j)-(r+j-1)*(r+j-1)+sum;
//cout<<sum<<endl;
				}
			}
	//	}
		outfile<<"Case #"<<i+1<<": "<<y<<endl;
	}
}
