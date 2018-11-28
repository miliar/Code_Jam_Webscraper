#include<iostream.h>
#include<sstream>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<fstream.h>
using namespace std;
main()
{
	ifstream in("A-small-attempt6.in");
	ofstream out("output.txt");
	int cases;
	in>>cases;
	int row1,row2;
int arr1[4];
int arr2[4];
int counter;
int joab;
	string s;
	for(int k=1;k<=cases;k++)
	{ counter=0;
		in>>row1;
		getline(in,s);
		for(int i=0;i<row1-1;i++)
		getline(in,s);
		for(int i=0;i<4;i++)
		in>>arr1[i];
		getline(in,s);
		for(int i=0;i<4-row1;i++)
		getline(in,s);
		in>>row2;
		getline(in,s);
		for(int i=0;i<row2-1;i++)
		getline(in,s);
		for(int i=0;i<4;i++)
		in>>arr2[i];
		getline(in,s);
		for(int i=0;i<4-row2;i++)
		getline(in,s);
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(arr1[i]==arr2[j])
			{
				counter++;
				joab=arr1[i];
			}
		}
		out<<"Case #"<<k<<": ";
		if(counter==0)
		out<<"Volunteer cheated!";
		else
		if(counter==1)
		out<<joab;
		else
		out<<"Bad magician!";
		if(k!=cases)
		out<<endl;
		
	}
}
