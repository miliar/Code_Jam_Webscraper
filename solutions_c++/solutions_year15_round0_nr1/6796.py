#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream f("input.txt");
	ofstream of;
	of.open("output.txt");
	int t;
	f>>t;
	int tt=1;
	while(t--)
	{
		int smax;
		string str;
		f>>smax>>str;
		int l=str.size();
		int sum=0;
		int count=0;
		for(int i=0;i<l;i++)
		{
			if(str[i]!='0')
			{
				sum += str[i]-'0';
			}
		else	if(str[i]=='0'&&str[i+1]!='0')
			{
				if(i+1>sum)
				{
				count += i+1-sum;
				sum += i+1-sum;
				
			}
//			  continue;
			  	
			}
			
		}
		of<<"Case #"<<tt<<": "<<count<<endl;
		tt++;
	}
}
