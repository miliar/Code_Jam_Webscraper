#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<cmath>
using namespace std;
void main()
{
	ifstream in;
	ofstream out;
	in.open("C-small-attempt1.in");
	out.open("C-small-attempt1.out");
	int t;
	in>>t;
	for(int i=1;i<=t;i++)
	{
		int num1,num2;
		int count=0;
		in>>num1;
		in>>num2;
		for(int j=num1;j<=num2;j++)
		{
			int k=j;
			string s="";
			while(k!=0)
			{
				int c=k%10;
				ostringstream ss;
                ss<<c;
                s=s+ss.str();
				k=k/10;
			}
			stringstream stream;
	        stream <<s;
	        int n;
			stream>>n;
			if(j==n)
			{
				double q=sqrt(static_cast<double>(j));
				if(q==static_cast<int>(q))
				{
					int u=static_cast<int>(q);
			        string st="";
			        while(u!=0)
			        {
				    int cc=u%10;
				    ostringstream ss;
                    ss<<cc;
                    st=st+ss.str();
			    	u=u/10;
			        }
	                stringstream stre;
	                stre <<st;
	                int nn;
			        stre>>nn;
			        if(nn==q)
						count++;
				}
			}
		}
		out<<"Case #"<<i<<": "<<count<<endl;
	}
}