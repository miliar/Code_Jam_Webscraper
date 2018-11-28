#include <iostream>
#include<stdio.h>
#include<fstream>
using namespace std;

int main()
{
	int t,cas;
	ifstream myfile;
	ofstream outpu;
	myfile.open("A-large.in");
	outpu.open("output.txt");
	cin>>t;
	cas = 1;
	while(t--)
	{
		int s;
		int total = 0;
		int ans = 0;
		cin>>s;
		for(int i = 0; i <=s ; i++)
		{
			char c;
			cin>>c;
			if(total < i)
			{
				ans += (i-total);
				total = i;
			}
			total += c - '0';
		}
		cout<<"Case #"<<cas<<": "<<ans<<"\n";
		cas++;
	}
}
