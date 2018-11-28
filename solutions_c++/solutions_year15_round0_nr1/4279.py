#include<iostream>
#include<algorithm>
#include<fstream>
#include<cstring>
using namespace std;

int main()
{
	int T,smax,ans,sum,t=1,len,i;
	char str[10010];
	fstream fin,fout;
	
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);

	fin>>T;
	cout<<T;
	
	while(t<=T)
	{
		fin>>smax;
		fin>>str;
		ans = 0;
		len = strlen(str);
		sum = str[0]-'0';
		for(i=1;i<len;i++)
		{
			if(sum<i)
			{
				ans+=(i-sum);
				sum = i;
			}
			sum+= (str[i]-'0');
		}
		fout<<"Case #"<<t<<": "<<ans<<"\n";
			
		t++;
	}
	
}
