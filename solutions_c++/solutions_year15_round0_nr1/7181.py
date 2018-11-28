//codejam #1
#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	ofstream out("clap.txt");
	long int t,n,i,no_friends,curr_no,l=1;
	string str;
	cin>>t;
	while(t--)
	{
		cin>>n>>str;

		no_friends=0;
		curr_no=0;
		for(i=1;i<=n;i++)
		{
			curr_no += ((int)str[i-1]-48);
		//	cout<<curr_no<<endl;
			if((str[i]!='0')&&(curr_no < i))
			{
					no_friends += (i-curr_no);
					curr_no += (i-curr_no);
			}
		}
		out<<"Case #"<<l<<": "<<no_friends<<endl;
		l++;
	}
	out.close();
	return 0;
}
