#include<iostream>
#include<string>
#include<cmath>
#include<fstream>
using namespace std;

bool isPal(int num)
{
	int n=num;
	int inv=0;
	while(n!=0)
	{
		inv=inv*10+n%10;
		n/=10;
	}
	return ((inv==num)? true:false);
}

bool isSqr(int num)
{
	if(sqrt(num)==static_cast<int>(sqrt(num))*1.0)return true;else return false;
}
int main()
{
	ifstream in("D://in.in");
	ofstream out("D://out.out");
	int t,line;
	
	in>>t;
	for(line=1;line<=t;line++)
	{
		int num=0;
		int a,b;
		in>>a>>b;
		for(;a<=b;a++)
			if(isPal(a)&&isSqr(a)&&isPal(sqrt(a)))num++;
		out<<"Case #"<<line<<": "<<num<<endl;

	}
	in.close();out.close();
	system("pause");return 0;
}