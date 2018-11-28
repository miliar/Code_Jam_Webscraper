#include<iostream>
#include<iomanip>
#include<stdlib.h>
#define min(a,b) (a<b?a:b)
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	
	cin.open("B_11.txt");
	cout.open("output_1.txt");
	
	
	int t,i;
	double c,f,x,r=2.0,s,MIN;
	cin>>t;
	cout<<fixed<<setprecision(7);
	
	for(i=1;i<=t;i++)
	{
		r=2.0;
		s=0;
		MIN=2000000000;
		cin>>c>>f>>x;
		
		while(1)
		{
			
			MIN=min(s+x/r,MIN);
			s+=(c/r);
			
			if(x/r<0.001)
			break;
			r+=f;
		}
		
		cout<<"Case #"<<i<<": "<<MIN<<endl;
		
		
		
		
	}
	
	cin.close();
	cout.close();
	
	return 0;
}