#include <iostream>
#include<string.h>
using namespace std;

int main() {
	int s,t,*a,i,sp=0,y,x,z=1;
	string p;
	cin>>t;
	while(t>0&&t<=100)
	{
		cin>>s;
		if(s>=0&&s<=6){
		cin>>p;
		a=new int[s+1];
		for(i=0;i<=s;i++)
		a[i]=p[i]-'0';
		x=0;y=0;
		sp=a[0];
		for(i=1;i<=s;i++)
		{
			if(i<=sp)
			sp=sp+a[i];
			else
			{
				
				x=i-sp;
				sp=sp+a[i]+x;
			y=y+x;	
			}
			
		}
		cout<<"case #"<<z<<": "<<y<<"\n";}
		z++;
		t--;
	}
	return 0;
}