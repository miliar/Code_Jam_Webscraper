                    //OM RAM JI
#include<stdio.h>
#include<string.h>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;

int main()
{
	int tc,r,t,count,j;
	ifstream ifile("d:/1.txt");
	ofstream ofile("d:/1ans.txt");
	ifile>>tc;
	
	for (j=0;j<tc;j++)
	{
		count=0;
		ifile>>r;
		ifile>>t;
		//cout<<r<<" "<<t<<endl;
		while (t>0)
		{
			if (t<((r+1)*(r+1)-r*r))
			{
				t=0;
			}
			else
			{
				count++;
				t=t-(r+1)*(r+1)+r*r;
			}
			r=r=r+2;
			//cout<<r<<" "<<t<<" "<<count<<endl;
		}
		ofile<<"Case #"<<j+1<<": "<<count<<endl;
	}
	return 0;
}
