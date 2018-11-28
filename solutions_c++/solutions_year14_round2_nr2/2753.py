#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("data.txt");
	out.open("out.txt");
	int loop;
	in>>loop;
	for(int z=1;z<=loop;z++)
	{
		int A,B,K;
	in>>A;
	in>>B;
	in>>K;
	int count =0;
	for (int i=0;i<A;i++)
	{
		for (int j=0;j<B;j++)
		{
			int x;
			x=i&j;
			if (x<K) count++;
		}
	}
	out<<"Case #"<<z<<": "<<count<<endl;
}
in.close();
out.close();
	return 0;
}
