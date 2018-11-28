#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;
int a[10001]={0},b[100001]={0};
long long x,y;
bool cmp(char a,char b)
{
	return a>b;
}
int main()
{
	string c;
	int t;
	ifstream ifs;
	ofstream ofs;

	ifs.open("in.txt");
	ofs.open("out.txt");

	ifs>>t;
	for(int i=1;i<=t;i++)
	{
		ifs>>c;
		sort(c.begin(),c.end(),cmp);
		ofs<<"Case #"<<i<<": "<<c<<"\n";
	}
	ifs.close();
	ofs.close();
}