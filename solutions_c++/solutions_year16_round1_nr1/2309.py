#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	long long t1,n;
	ifstream inp("input.txt");
	ofstream out("output.txt");
	string line;
	inp>>t1;
	for(long long it=1;it<=t1;it++)
	{
		char s[1003],max,ans[2002],start=1001,end=1001;
		inp>>s;
		max=s[0];
		ans[start--]=max;
		for(int i=1;s[i]!='\0';i++)
		{
			if(s[i]>=max)
			{
				max=s[i];
				ans[start--]=max;
			}
			else
			{
				end++;
				ans[end]=s[i];
			}
		}
		ans[++end]='\0';
		out<<"Case #"<<it<<": "<<ans+start+1<<endl;	
	}
	out.close();
}
