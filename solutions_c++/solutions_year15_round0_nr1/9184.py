#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>> t;
	int q;
	q=1;
	while(q<=t)
	{
		int s;
		cin>> s;
		string a;
		int b[s+1];
		int i, x, y, z;
		cin>> a;
		x=0;//x is the number of people required
		for(i=0;i<=s;i++)
		{
			b[i]=a[i]-'0';
		}
		y=b[0];//number of people standing already
		for(i=1;i<=s;i++)
		{
			z=0;
			if(y<i&&b[i]!=0)
			{
				z=i-y;
				x+=z;
			}
			y+=z+b[i];//updating people standing
		}
		cout<< "Case #"<<q<<":"<<" "<< x<< endl;
		q++;
	}
}
