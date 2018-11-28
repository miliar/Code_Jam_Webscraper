#include<fstream>
#include<string>
using namespace std;
main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
	int t;
	in>>t;
	int c=1;
	while(c<=t)
	{
		int sum=0,x,count=0;
		string s;
		in>>x;
		in>>s;
		for(int k=0;k<=x;k++)
		{
			int temp=s[k]-'0';
			if (temp!=0)
				if(sum>=k)
					sum+=temp;
				else{
					count+=k-sum;
					sum+=k-sum+temp;
				}		
		}
		out<<"Case #"<<c<<": "<<count<<endl;
		c++;
	}
}