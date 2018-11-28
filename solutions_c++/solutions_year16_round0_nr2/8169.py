#include<bits/stdc++.h>
using namespace std;
#define LL long long
int main()
{
	ifstream in;
	ofstream op;
  	in.open ("B-large.in");
  	op.open("output2.txt");
	int t;
	in>>t;
	for(int i=1;i<=t;i++)
	{
		int times=0;
		string str;
		in>>str;
		int l=str.length();
		bool pos=true;
		for(int j=l-1;j>=0;j--)
		{
			if(str[j]=='-')
			{
				pos=false;
				times++;
				bool temp=true;
				for(j=j-1;j>=0;j--)
				{
					if(str[j]=='+')
						temp=true;
					else 
						temp=false;
					if(temp!=pos)
					{
						times++;
						pos=temp;
					}
				}
			}
		}
		op<<"Case #"<<i<<": "<<times<<"\n";
	}
	in.close();
	op.close();
	return 0;
}
