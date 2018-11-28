#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
	unsigned int a,b,c,k,count,cases,t;
	ifstream fin;
	ofstream fout;
	fin.open("input.txt",ios::in);
	fout.open("output.txt");
	//cin>>cases;
	fin>>cases;
	t=1;
	while(t<=cases)
	{
		//cin>>a>>b>>k;
		fin>>a>>b>>k;
		//cout<<a<<" "<<b<<" "<<k<<"\n";
		count = 0;
		for(int i=0 ; i<a ; ++i)
			for(int j=0 ; j<b ; ++j)
			{
				c = (i&j);
				if(c<k)
					count++;
			}
		//cout<<"Case #"<<t<<": "<<count<<"\n";
		fout<<"Case #"<<t<<": "<<count<<"\n";
		t++;
	}
	fin.close();
	fout.close();
	return 0;
}
