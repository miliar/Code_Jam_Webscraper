#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		cin>>s;
		int x=s.length();
		int a[26]={0};
		int b[10]={0};
		char c;
		for(int j=0;j<x;j++)
		{
			c=s.at(j);
			a[int(c)-65]++;
		}
		while(a[25]>0)
		{
			b[0]++;
			a[25]--;
			a[4]--;
			a[17]--;
			a[14]--;
		}
		while(a[23]>0)
		{
			b[6]++;
			a[18]--;
			a[8]--;
			a[23]--;
		}
		while(a[6]>0)
		{
			b[8]++;
			a[4]--;
			a[8]--;
			a[6]--;
			a[7]--;
			a[19]--;
		}
		while(a[22]>0)
		{
			b[2]++;
			a[19]--;
			a[22]--;
			a[14]--;
		}
		while(a[20]>0)
		{
			b[4]++;
			a[5]--;
			a[14]--;
			a[20]--;
			a[17]--;
		}
		while(a[18]>0)
		{
			b[7]++;
			a[18]--;
			a[4]--;
			a[21]--;
			a[4]--;
			a[13]--;
		}
		while(a[7]>0)
		{
			b[3]++;
			a[19]--;
			a[7]--;
			a[17]--;
			a[4]--;
			a[4]--;
		}
		while(a[14]>0)
		{
			b[1]++;
			a[14]--;
			a[13]--;
			a[4]--;
		}
		while(a[21]>0)
		{
			b[5]++;
			a[5]--;
			a[8]--;
			a[21]--;
			a[4]--;
		}
		while(a[13]>0)
		{
			b[9]++;
			a[13]--;
			a[8]--;
			a[13]--;
			a[4]--;
		}
		cout<<"Case #"<<(i+1)<<": ";
		for(int j=0;j<10;j++)
		{
			while(b[j]>0)
			{
				cout<<j;
				b[j]--;
			}
		}
		cout<<endl;
	}
	return 0;
}