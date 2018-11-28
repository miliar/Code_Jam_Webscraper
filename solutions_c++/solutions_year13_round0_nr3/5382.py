#include<fstream>
#include<iostream>
using namespace std;
int main()
{
	ifstream indd;
	ofstream outd;
	indd.open("C-small-attempt4.in");
	outd.open("C-small-attempt0.out");
	int num;
	indd>>num;
	//cin>>num;
	for(int i=1;i<=num;i++)
	{
		outd<<"Case #"<<i<<": ";
		int a,b;
		indd>>a>>b;
		//cin>>a>>b;
		int count=0;
		for(int j=a;j<=b;j++)
			if(j==1||j==4||j==9||j==121||j==484)
				count++;
		//cout<<count<<endl;
		outd<<count<<endl;
	}
	return 0;
}