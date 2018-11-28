#include <iostream>
#include <fstream>
using namespace std;

const int MAX_N=1000;

int main(int argc, char** agrv)
{
	ifstream inf("in.txt",ios_base::in);
	ofstream ouf("out.txt",ios_base::out);
	//istream &inf=cin;
	//ostream &ouf=cout;
	
	int T;
	int N;
	int m[MAX_N];
	inf>>T;
	for(int x=1;x<=T;++x)
	{
		inf>>N;
		for(int i=0;i<N;++i) inf>>m[i];
		
		int y=0,z=0;
		int max_fall=0;
		
		for(int i=0;i<N-1;++i)
		{
			if(m[i]-m[i+1]>0)
			{
				y += m[i]-m[i+1];
				if(m[i]-m[i+1]>max_fall) 
					max_fall = m[i]-m[i+1];
			}
		}
		for(int i=0;i<N-1;++i)
		{
			if(m[i]>max_fall)
				z += max_fall;
			else
				z += m[i];
		}
		
		ouf<<"Case #"<<x<<": "<<y<<" "<<z<<endl;
	}
	return 0;
}