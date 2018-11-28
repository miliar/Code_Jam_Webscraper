#include<iostream>
#include<string>
using namespace std;
int main()
{
	int T;
	cin>>T;
	int temp=0;
	while(temp<T)
	{
		string a;
		string s;
		cin>>a;
		int k=0;
		int b[2000];
		while(k<a.length())
		{
			b[k]=(int)a[k];
			k++;	
		}
		s=s+a[0];
		k=1;
		int z=0;
		while(k<a.length())
		{
			if((int)s[0]>b[k])
			{
				s=s+a[k];
			}
			else
			{
				s=a[k]+s;
			}
			k++;	
		}
		cout<<"Case #"<<(temp+1)<<": ";
		for(int i=0;i<s.length();i++)
		{
			cout<<s[i];
		}
		cout<<endl;
		temp++;
	}
	return 0;
}