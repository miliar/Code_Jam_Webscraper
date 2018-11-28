#include<iostream.h>
#include<fstream>
using namespace std;
 main()
{
ifstream in("A-large.in");//input file
ofstream out("output.txt");//output file
int test; //  test as4
in >> test; // must be continoues

for(int i=1;i<=test;i++)
{
	int sum=0;
	int leng; // also test
	in >> leng;
	string str; // the input
	in >> str;
			int c=0; // counter for audience
	for(int i=0;i<str.size();i++)
	{
		int temp=str[i]-'0';
		if(temp == 0)
			continue;
		if(i<=sum)
			sum+=temp;
		else{
			c+=(i-sum);
			sum+=(i-sum+temp);
		}
	}
	out<<"Case #"<<i<<": "<<c<<endl;
}
}