#include<iostream>
#include<string>
using namespace std;
int main()
{
	int test_case,smax,count,len,extra=0,case_count=0;
	string s;
	cin>>test_case;
	while(test_case)
	{
		cin>>smax;
		cin>>s;
		count=0;
		len=s.size();
		extra=0;
		for(int i=0;i<len;i++)
		{
			if(count>=i)
			{
				count=count+(s[i]-48);
			}
			else
			{
				extra = extra + (i-count);
				count = count + (i-count)+ (s[i]-48);
			}
		}
		case_count++;
		cout<<"Case #"<<case_count<<": "<<extra<<endl;
		test_case--;



	}
	return 0;
}
