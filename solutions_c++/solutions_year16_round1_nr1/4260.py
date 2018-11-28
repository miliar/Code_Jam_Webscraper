#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

main()
{
	string a,b;
	long long int i,j,len,t;
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("codejam_c2q1.out");
	in>>t;
	for(j=1;j<=t;j++)
	{
		in>>a;
//		cout<<a<<endl;
		len=a.length();
		b=a[0];
//		cout<<b<<endl<<endl;
		i=1;
		while(i<len)
		{
			if(a[i]>=b[0])
			{
				b.insert(0,1,a[i]);
			}
			else
			{
				b=b+a[i];
			}
//			cout<<b<<" ";
			i++;
		}
//		cout<<endl;
		out<<"Case #"<<j<<": "<<b<<endl;
	}
}
