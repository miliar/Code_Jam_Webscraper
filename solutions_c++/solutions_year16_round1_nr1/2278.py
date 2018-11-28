#include <iostream>
#include <cstring>
using namespace std;
int main() 
{
	long long int t,i,len,start,end,j;
	char str[2000],ans[5000];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>str;
		len=strlen(str);
		ans[2000]='a';
		ans[2002]='a';
		ans[2001]=str[0];
		start=2001;
		end=2001;
		for(j=1;j<len;j++)
		{
			if(str[j]<ans[start])
			{
				end++;
				ans[end]=str[j];
			}
			else
			{
				start--;
				ans[start]=str[j];
			}
		}
		cout<<"Case #"<<i+1<<": ";
		for(j=start;j<=end;j++)
		{
			cout<<ans[j];
		}
		cout<<endl;
	}
	return 0;
}