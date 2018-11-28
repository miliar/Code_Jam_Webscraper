#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main()
{
	int t;
//	cin>>t;
	int n;
	int m=0;
	string s1;
	freopen("out01.txt","w",stdout);
	cin>>s1;
	while(1)
	{
		m++;
		string s;
//		cin>>n;
		cin>>s;
		cin>>s;
		int counter=0;
		int sum=0;
		for(int i=0;i<=s.size()-1;i++)
		{
			if(i>counter)
			{
				sum+=(i-counter);
				counter=i;
			}
			counter+=s[i]-'0';
		}
		cout<<"Case #"<<m<<": "<<sum<<endl;
	}
	fclose(stdout);
	return 0;
}
