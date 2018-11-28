#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
	int T;
	int N;
	string S;
	int y;
	
	ifstream inf("in.txt",ios_base::in);
	//cout<<"Open!"<<endl;
	inf>>T;
	ofstream ouf("out.txt");
	//cout<<"Open!"<<T<<endl;
	for(int x=1;x<=T;++x)
	{
		inf>>N>>S;
		y = 0;
		int sum = 0;
		//cout<<x<<endl;
		for(int i =0;i<N;++i)
		{
			sum += S[i] - '0';
			if(i+1-sum>y) y = i+1-sum;
		}
		ouf<<"Case #"<<x<<": "<<y<<endl;
		//cout<<"Case#"<<x<<": "<<y<<endl;
	}
	ouf.close();
	inf.close();
	return 0;
}