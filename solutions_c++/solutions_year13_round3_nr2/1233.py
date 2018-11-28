#include<fstream>
//#include<set>
#include<string>
using namespace std;

string east(long x)
{
	string t;
	if (x==0)
	{
		t="";
	}
	if (x>0)
	{
		for (int i=0; i!=x; ++i)
		{
			t+="WE";
		}
	}	
	if (x<0)
	{
		for (int i=0; i!=-x; ++i)
		{
			t+="EW";
		}
	}
	return t;
}

string north(long x)
{
	string t;
	if (x==0)
	{
		return "";
	}
	if(x>0){
	for (int i=0; i!=x; ++i)
	{
		t+="SN";
	}
	}	
	if(x<0){
	for (int i=0; i!=-x; ++i)
	{
		t+="NS";
	}
	}
	return t;
}

int main()
{
	long n;
	ifstream infile("R1CB.in");
	ofstream ofile("R1CB.txt");

	infile>>n;
	long x,y;
	for (long i=0; i!=n; ++i)
	{
		infile>>x>>y;
		ofile<<"Case #"<<i+1<<": "<<east(x)<<north(y)<<endl;
	}
	infile.close();
	ofile.close();
	return 0;
}
