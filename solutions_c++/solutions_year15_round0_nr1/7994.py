#include<iostream>
#include<fstream>

using namespace std;

main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("in.txt");
	outfile.open("out.txt");
	int tests,i;
	infile >> tests;
	for(i=1;i<=tests;i++)
	{
		int levels,j,stand=0,count=0;
		char arr[1005];
		infile >> levels;
		infile >> arr;
		for(j=0;j<=levels;j++)
		{
			if(arr[j]-'0'>0)
			{
				if(stand+count >= j)
				{
					stand+=arr[j]-'0';
				}
				else
				{
					count = j - stand;
					stand+=arr[j]-'0';
				}
			}
			
		}
		outfile <<"Case #"<<i<<": "<<count<<endl;
	}
}
