#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int calc()
{
	int x,r,c;
	cin>>x>>r>>c;
	
	if(r*c%x!=0)return -1;
	switch(x)
	{
		case 1:
		case 2:
		return 1;
		
		case 3:
		if(min(r,c)<2)return -1;
		else return 1;
		
		case 4:
		if(min(r,c)<3)return -1;
		else return 1;
		default: cerr<<"strange x"<<x<<","<<r<<","<<c<<endl;
		return 0;
	}
}

int main()
{
	//cout<<calc();return 0;
	int N;cin>>N;
	for(int i=0;i<N;i++)
		cout<<"Case #"<<(i+1)<<": "<<(calc()>0?"GABRIEL":"RICHARD")<<endl;
	return 0;
}