#include <iostream>
#include <fstream>
using namespace std;
int main()
{	ofstream fout;
	fout.open("jamans.txt");
	int cases,ca=1;
	cin>>cases;
	while(cases-->0)
	{
		int ans,ans1;
		int c=0,b[16],d[4],d1[4],x;
		cin>>ans;
		while(c<16)
		{	cin>>x;
			b[c++]=x;
		}int n=0,n1,v;
		n1=(ans-1)*4;
		cout<<n1<<endl;
		while(n<4)
			d[n++]=b[n1++];
		cin>>ans1;
		c=0;
		while(c<16)
		{	cin>>x;
			b[c++]=x;
		}
		n=0;
		n1=(ans1-1)*4;
		while(n<4)
			d1[n++]=b[n1++];
		int n2=0,n3=0;c=0;
		while(n2<4)
		{	n3=0;

			while(n3<4)
			{ 
				if(d[n2]==d1[n3])
					{	c++;
						v=d[n2];
					}
				n3++;
			}
			n2++;
		}
		if(c==1)
		{	fout<<"Case #"<<ca<<": "<<v<<endl;

		}
		else if(c==0)
		{	fout<<"Case #"<<ca<<": "<<"Volunteer cheated!"<<endl;

		}
		else
		{
			fout<<"Case #"<<ca<<": "<<"Bad magician!"<<endl;
		}
		ca++;
	}
}