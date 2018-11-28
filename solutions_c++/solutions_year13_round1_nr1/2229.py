#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<math.h>
using namespace std;

int main()
{
	ifstream file("A-small-attempt0.in");
	cin.rdbuf(file.rdbuf());
	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	long long T,r,t;
	cin>>T;
	for(int x=0;x<T;x++)
	{
		cin>>r>>t;
		long long fb = 1-2*r;
		unsigned long long sq = (2*r-1)*(2*r-1)+8*t;
		long double s = sqrt((long double)sq);
		unsigned long long res = (fb+s)/4;
		
		//cout<<fb<<"  "<<sq<<"  "<<s<<"  "<<fb+s<<endl;
		cout<<"Case #"<<x+1<<": "<<res<<endl;
	}

	return 0;
}
		