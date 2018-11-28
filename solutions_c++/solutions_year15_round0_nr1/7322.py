#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	long t,s,frnd,i,j,k,n,ppl;
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("CJ_q1_output.out");
	in>>t;
	char c;
	for(i=1;i<=t;i++)
	{
		in>>s;
		frnd=0;
		ppl=0;
		for(j=0;j<=s;j++)
		{
			in>>c;
			n=c%48;
			if(j==0)
			{
				ppl+=n;
				continue;
			}
			if(ppl+frnd>=j)
			{
				ppl+=n;
			}
			else if(n>0)
			{
				frnd=j-ppl;
				ppl+=n;
			}
//			cout<<frnd<<" "<<ppl<<"\n";
		}
		out<<"Case #"<<i<<": "<<frnd<<endl;		
	}
	in.close();
	out.close();
	return 0;
}
