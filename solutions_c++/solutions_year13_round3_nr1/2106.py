#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int test;
	cin>>test;
	int c = 1;
	while(test--)
	{
		string str;
		int n;
		cin>>str>>n;
		int count = 0, sum = 0,num = 0,pos = 0,total;
		
		for(int i = 0; i<str.length(); i++)
		{
			if(str[i] == 'a' ||str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u')
			{
				count = 0;
			}
			else
				count++;
			if(count >= n)
			{
				num++;
				if(num == 1)
					 total = i-(n-1)+str.length()-i+((i-(n-1))*(str.length()-i-1));
				else
					total = (str.length()-i-1)+(i-n)-pos+1+((str.length()-i-1)*((i-n)-pos));
				sum = sum + total;
				pos = i-(n-1);
			}
		}
		cout<<"Case #"<<c<<": "<<sum<<endl;
		c++;
	}
	return 0;
}
