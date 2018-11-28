#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int test_count;
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("output");

	in>>test_count;
	
	int s_max;
	string s;
	int count=1;
	
	while(count<=test_count)
{
	int extra=0;
	int total=0;
	
	
	in>>s_max;
	in>>s;
	for(int i=0;i<=s_max;i++)
	{
		int a=s.at(i)-'0';
		if(total<i)
		{
			total++;
			extra++;
		}
		total+=a;
	}
	out<<"case #"<<count<<": "<<extra<<endl;
	count++;
}

return 0;
}
