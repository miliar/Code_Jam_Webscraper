#include <iostream>
#include <fstream>
using namespace std;
#define lld long long
fstream fin,fout;
char s[1005];
int main()
{
	int t,smax,i,j;

	//fin.open("input.txt");
	fout.open("output1.txt");

	//fin>>t;
	cin>>t;
	
	//while(t--)
	for(j=1;j<=t;j++)
	{
		//fin>>smax;
		//fin>>s;
		cin>>smax;
		cin>>s;

		//cout<<smax<<" "<<s<<"\n";
		lld sum=0,req=0;

		sum+=s[0]-'0';
		for(i=1;i<=smax;i++)
		{
			if(sum<i&&s[i]!='0')
			{
				req+=(i-sum);
				sum=i;
			}
			sum+=s[i]-'0';

		}
		fout<<"Case #"<<j<<": "<<req<<"\n";
	}



}