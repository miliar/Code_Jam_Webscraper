#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int t;
	ofstream out;
	out.open("A-small-attempt0.out");
	ifstream in;
	in.open("A-small-attempt0.in");
	in>>t;
	int x,y,a[4][4],b[4][4];
	for(int n=1;n<=t;n++)
	{
	bool present[17]={false};
	in>>x;
	for(int i=0;i<4;i++)
	{
	for(int j=0;j<4;j++)
	{
	in>>a[i][j];
	if(i==x-1)
	present[a[i][j]]=true;
	}
	}
	in>>y;
	int count=0,val;
	for(int i=0;i<4;i++)
	{
	for(int j=0;j<4;j++)
	{
	in>>b[i][j];
	if(i==y-1 && present[b[i][j]])
	{val=b[i][j];count++;}
	}
	}
	out<<"Case #"<<n<<": ";
	if(count==0)
	out<<"Volunteer cheated!\n";
	else if(count>1)
	out<<"Bad magician!\n";
	else
	out<<val<<"\n";
	}
	return 0;
}
