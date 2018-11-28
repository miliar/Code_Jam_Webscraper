#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
{
	int t,t1=1;
	cin >> t;
	while(t1<=t)
	{
		long int n;
		cin >> n;
		int array[10]={0},sum=0,i=1,j,temp,flag=0;
		if(n==0)
		{
			cout << "Case #" <<t1<<":"<<" "<<"INSOMNIA"<<endl;
		}
		else
		{	
			while(sum!=10)
			{
				sum=0;
				flag=1;
				string s=to_string(n*i);
				for(j=0;j<(int)s.size();j++)
				{
					temp=s[j]-'0';
					array[temp]=1;
				}
				for(j=0;j<10;j++)
				{
					sum+=array[j];
				}
				i++;
			}
			if(flag==1)
				cout << "Case #" <<t1<<":"<<" "<<n*(i-1)<<endl;
			else
				cout << "Case #" <<t1<<":"<<" "<<n*1<<endl;
		}
		t1++;
	}
	return 0;
}